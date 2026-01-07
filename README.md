
#  Park Accessibility Analysis: KD-Tree and Network Analysis

This repository presents a Python toolkit for evaluating urban park accessibility using two spatial approaches: **KD-Tree-based Euclidean distance** and **network-based walking distance** analysis. This project generates reproducible outputs suitable for urban planning applications.

## 📋 Overview

Urban green spaces are crucial for public health, climate resilience, and environmental equity. This project provides methods to quantify and visualize park accessibility at the building level.

##  Methodological Approaches

### 1️⃣ **KD-Tree-Based Accessibility (Euclidean Distance)**
The KD-tree approach is used to identify and visualize parks that lie within a 500 m straight-line (Euclidean) distance from residential buildings.

**Objective:** Fast identification of accessible parks using straight-line distances.
- **Advantages:** Extremely fast O(log n) queries, scales to city-level datasets
- **Limitations:** Doesn't account for street networks or barriers
- **Best for:** Exploratory analysis and comparative studies

### 2️⃣ **Network-Based Accessibility (Walking Distance)**
The network-based approach evaluates park accessibility using pedestrian street networks, classifying buildings within 1,500 m walking distance of the nearest park and those that fall beyond the threshold (interpreted as having limited access).

**Objective:** Realistic walking accessibility using pedestrian street networks.
- **Advantages:** Accounts for street connectivity and real walking routes
- **Limitations:** Computationally more expensive
- **Best for:** Planning, policy applications, and detailed assessments

##  Data Sources

- **Administrative boundaries:** PDOK (Kadaster, Netherlands) – municipality boundaries via WFS
- **Parks:** OpenStreetMap (`leisure=park`)
- **Buildings:** OpenStreetMap (`building=*`)
- **Walking network:** OpenStreetMap pedestrian street network


## 📂 Repository Structure

```
├── main.py                     # Entry point for KD-Tree workflow                
├── outputs/
│   └── KDoutput/
│   |    ├── accessibility_map.html
│   |    └── accessibility_bar.png  
|   |
|   |── NA_outputs/      # Creates after running python main.py
├                
├── src/
│   └── park_accessibility/
│       ├── kd_park_accessibility/
│       │   ├── downloader.py   # Data acquisition
│       │   ├── geo.py          # Geometry handling
│       │   ├── kdtree.py       # KD-Tree construction and queries
│       │   ├── service.py      # Accessibility logic
│       │   └── viz.py          # Visualization (HTML/PNG)
│       └── NA_park_accessibility/
│           ├── NA_data_processing.py
│           ├── NA_analysis.py
│           ├── NA_visualization.py
│           └── __init__.py
├── test/
    ├── test_accessibility.py
    ├── test_api.py
    ├── test_downloader.py
    ├── test_geo.py
    └── test_kdtree.py                      # Unit tests
├── pyproject.toml              # Project configuration
├── poetry.lock                 # Dependency lock file
└── README.md
```

## ⚙️ Installation & Setup

This project uses **Poetry** for dependency management.

### 1️⃣ Install Poetry (if not installed)
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 2️⃣ Clone and install dependencies
```bash
git clone https://github.com/pratistha-katwal/Park_Accessibility_
cd Park_Accessibility_
poetry install
```

### 3️⃣ Activate the virtual environment
```bash
poetry shell
```

## ▶️ Running the Analyses

### **KD-Tree Accessibility Analysis**
```bash
python main.py
```

**Outputs:** Generated in `outputs/KDoutput/`
- `accessibility_map.html` - Interactive map
- `accessibility_bar.png` - Summary visualization

### **Network-Based Accessibility Analysis**
```bash
python main.py
```

**Outputs:** Generated in `outputs/NA_outputs/` (created automatically after running)
```
│   ├── ams_boundary.gpkg
│   ├── amsterdam_park_accessibility.html #Interactive map
│   ├── amsterdam_park_accessibility_bar.png
│   ├── amsterdam_park_accessibility_matplotlib.png
│   ├── buildings_ams.gpkg
│   ├── buildings_park_access_1500m.gpkg
│   ├── distance_vs_access.png
│   ├── parks_ams.gpkg
│   ├── walking_edges_ams.gpkg
│   └── walking_nodes_ams.gpkg
```

## 📊 Results Interpretation - Amsterdam Case Study Results

###  **Data Overview**
- Total buildings: 197,057
- Buildings with park access within 1500 m: 190,120 (96.5%)
- Buildings without park access within 1500 m: 6,937 (3.5%)

###  **Distance Statistics (Walking Distance)**
- Minimum distance to nearest park: 0.0 m
- Maximum distance to nearest park: 1,499.76 m
- Mean distance to nearest park: 469.95 m

##  Viewing Interactive Maps

### Local Viewing
```bash
# KD-Tree results
open outputs/KDoutput/accessibility_map.html

# Network Analysis results
open outputs/NA_outputs/amsterdam_park_accessibility.html
```

##  Testing

Run unit tests to ensure robustness:
```bash
pytest
```

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **GeoPandas** | Geospatial data manipulation |
| **OSMnx** | Street network data retrieval |
| **NetworkX** | Network analysis and routing |
| **SciPy** | KD-Tree implementation |
| **Folium/Plotly** | Interactive visualizations |
| **Poetry** | Dependency management |
| **PyTest** | Testing framework |

##  Development Notes

**Project Architecture**
- **Modular Design:** Separate modules for KD-Tree and Network Analysis
- **Data Pipeline:** Automated data download → processing → analysis → visualization
- **Reproducibility:** Deterministic outputs with version-controlled dependencies
- **Branch History:** The KD-Tree and Network Analysis workflows were developed in separate Git branches for independent testing and optimization before merging into the main branch.
- **Reproducibility:** All outputs are static and deterministic, ensuring reproducible results across runs.


##  Applications & Use Cases

- **Urban Planning:** Identify accessibility gaps and prioritize park development
- **Public Health:** Correlate park access with health outcomes
- **Environmental Justice:** Assess equitable distribution of green spaces
- **Real Estate:** Evaluate neighborhood amenities
- **Academic Research:** Comparative spatial analysis methodologies

---

## 🔗 References
- OpenStreetMap: https://www.openstreetmap.org
- PDOK (Kadaster): https://www.pdok.nl
- NetworkX library: https://networkx.org
```
