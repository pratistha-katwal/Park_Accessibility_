from __future__ import annotations

import json
import math
from pathlib import Path
from typing import List, Tuple

import matplotlib.pyplot as plt
import folium

from src.park_access.geo import haversine_m
from src.park_access.kdtree import build_park_kdtree, nearest_park


# ---------- Load + centroids ----------

def load_parks_geojson(path: str = "data/parks.geojson") -> List[dict]:
    geo = json.loads(Path(path).read_text(encoding="utf-8"))
    return geo["features"]


def _centroid_of_polygon(coords: List[Tuple[float, float]]) -> Tuple[float, float]:
    """
    coords: list of (lon, lat) tuples for outer ring (closed)
    returns (lat, lon)
    """
    if len(coords) < 3:
        xs = [c[0] for c in coords]
        ys = [c[1] for c in coords]
        return (sum(ys) / len(ys), sum(xs) / len(xs))

    a = 0.0
    cx = 0.0
    cy = 0.0
    for i in range(len(coords) - 1):
        x0, y0 = coords[i]
        x1, y1 = coords[i + 1]
        cross = x0 * y1 - x1 * y0
        a += cross
        cx += (x0 + x1) * cross
        cy += (y0 + y1) * cross

    if abs(a) < 1e-12:
        xs = [c[0] for c in coords]
        ys = [c[1] for c in coords]
        return (sum(ys) / len(ys), sum(xs) / len(xs))

    a *= 0.5
    cx /= (6.0 * a)
    cy /= (6.0 * a)
    return (cy, cx)  # lat, lon


def extract_park_centroids(parks_geojson_path: str = "data/parks.geojson") -> List[dict]:
    feats = load_parks_geojson(parks_geojson_path)
    parks = []
    for f in feats:
        geom = f.get("geometry", {})
        if geom.get("type") != "Polygon":
            continue
        coords = geom.get("coordinates", [])
        if not coords or not coords[0]:
            continue

        ring = coords[0]  # outer ring
        ring_tuples = [(pt[0], pt[1]) for pt in ring]  # (lon, lat)
        lat, lon = _centroid_of_polygon(ring_tuples)

        parks.append(
            {
                "name": (f.get("properties", {}) or {}).get("name") or "Unnamed park",
                "lat": float(lat),
                "lon": float(lon),
            }
        )
    return parks


# ---------- Grid sampling ----------

def make_grid_points(parks: List[dict], step_deg: float = 0.003) -> List[Tuple[float, float]]:
    """
    Creates a grid over the bounding box of the parks.
    step_deg ~ 0.003 is a few hundred meters in NL.
    Returns list of (lat, lon).
    """
    lats = [p["lat"] for p in parks]
    lons = [p["lon"] for p in parks]

    min_lat, max_lat = min(lats), max(lats)
    min_lon, max_lon = min(lons), max(lons)

    # Small padding
    pad_lat = (max_lat - min_lat) * 0.05
    pad_lon = (max_lon - min_lon) * 0.05
    min_lat -= pad_lat
    max_lat += pad_lat
    min_lon -= pad_lon
    max_lon += pad_lon

    pts = []
    lat = min_lat
    while lat <= max_lat:
        lon = min_lon
        while lon <= max_lon:
            pts.append((lat, lon))
            lon += step_deg
        lat += step_deg
    return pts


# ---------- Bar chart ----------

def save_bar_chart(accessible: int, inaccessible: int, out_path: str = "outputs/accessibility_bar.png"):
    total = accessible + inaccessible
    acc_pct = 100.0 * accessible / total
    inac_pct = 100.0 * inaccessible / total

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    plt.figure()
    plt.bar(["Accessible (<500m)", "Not Accessible (>=500m)"], [acc_pct, inac_pct])
    plt.ylabel("Percentage (%)")
    plt.title("Park Accessibility (percentage of sampled points)")
    plt.ylim(0, 100)
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()


# ---------- Folium map ----------

def save_folium_map(
    parks: List[dict],
    inaccessible_points: List[Tuple[float, float]],
    out_path: str = "outputs/accessibility_map.html",
):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    # Center map on average park location
    center_lat = sum(p["lat"] for p in parks) / len(parks)
    center_lon = sum(p["lon"] for p in parks) / len(parks)

    m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Parks in green
    for p in parks:
        folium.CircleMarker(
            location=[p["lat"], p["lon"]],
            radius=4,
            popup=p["name"],
            fill=True,
        ).add_to(m)

    # Inaccessible points in red (sample only to keep file size reasonable)
    # If there are many points, plotting all can make the HTML huge.
    max_points = 1500
    pts = inaccessible_points[:max_points]
    for (lat, lon) in pts:
        folium.CircleMarker(
            location=[lat, lon],
            radius=2,
            fill=True,
        ).add_to(m)

    m.save(out_path)


# ---------- Main script ----------

def main():
    parks = extract_park_centroids()
    print(f"Loaded {len(parks)} parks (centroids)")

    tree, meta = build_park_kdtree(parks)

    grid = make_grid_points(parks, step_deg=0.003)

    accessible = 0
    inaccessible = 0
    inaccessible_pts: List[Tuple[float, float]] = []

    for (lat, lon) in grid:
        p = nearest_park(tree, meta, lat, lon)
        d = haversine_m(lat, lon, p["lat"], p["lon"])
        if d < 500:
            accessible += 1
        else:
            inaccessible += 1
            inaccessible_pts.append((lat, lon))

    print(f"Accessible points: {accessible}")
    print(f"Inaccessible points: {inaccessible}")

    save_bar_chart(accessible, inaccessible, "outputs/accessibility_bar.png")
    print("Saved bar chart to outputs/accessibility_bar.png")

    save_folium_map(parks, inaccessible_pts, "outputs/accessibility_map.html")
    print("Saved map to outputs/accessibility_map.html")


if __name__ == "__main__":
    import folium

    parks = extract_park_centroids("data/parks.geojson")
    print(f"Loaded {len(parks)} parks (centroids)")

    # Create base map (Amsterdam)
    m = folium.Map(location=[52.37, 4.89], zoom_start=12)

    # Plot parks in green
    for p in parks:
        folium.CircleMarker(
            location=[p["lat"], p["lon"]],
            radius=3,
            color="green",
            fill=True,
            fill_opacity=0.7,
            popup=p["name"] or "Park",
        ).add_to(m)

    # Ensure outputs folder exists
    Path("outputs").mkdir(exist_ok=True)

    # SAVE MAP (this was missing!)
    m.save("outputs/accessibility_map.html")

    print("Saved map to outputs/accessibility_map.html")
