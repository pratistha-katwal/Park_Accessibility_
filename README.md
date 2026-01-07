🌳 Park Accessibility Analysis using KD-Tree and Network Analysis

This repository presents a comprehensive urban park accessibility analysis implemented in Python using two complementary spatial approaches:

KD-Tree–based Euclidean accessibility

Network-based walking accessibility

The project generates static, reproducible outputs including interactive HTML maps and summary visualizations, which can be published as a website using GitHub Pages.

📌 Project Motivation

Access to urban green spaces is a key indicator of:

Urban livability

Public health

Climate resilience

Environmental equity

This project evaluates how accessible parks are to buildings using both computationally efficient and realistic network-based methods, enabling comparison between simplified and real-world accessibility metrics.

🧠 Methodological Approaches
1️⃣ KD-Tree–Based Accessibility (Euclidean Distance)

Objective:
Estimate the nearest park for each building using straight-line (Euclidean) distance.

Why KD-Tree?

Extremely fast for large datasets

Scales well to city-level analysis

Suitable for exploratory and comparative studies

Limitations:

Does not account for street networks or barriers

Represents idealized accessibility

Key implementation:

src/park_accessibility/kd_park_accessibility/
├── downloader.py   # Data acquisition
├── geo.py          # Geometry handling
├── kdtree.py       # KD-Tree construction and queries
├── service.py      # Accessibility logic
└── viz.py          # Visualization (HTML / PNG)


Outputs:

Interactive accessibility map (HTML)

Summary plots (PNG)

2️⃣ Network-Based Accessibility (Walking Distance)

Objective:
Compute realistic walking accessibility to parks using pedestrian street networks.

Why Network Analysis?

Accounts for street connectivity

Reflects real walking distances

More suitable for planning and policy applications

Trade-off:

Computationally more expensive than KD-Tree

Requires careful network preprocessing

Key implementation:

src/park_accessibility/NA_park_accessibility/
├── NA_data_processing.py
├── NA_analysis.py
├── NA_visualization.py
└── __init__.py

📂 Repository Structure
├── main.py                     # Entry point (KD-Tree workflow)
├── NA_main.py                  # Entry point (Network Analysis workflow)
├── outputs/
│   └── KDoutput/
│       ├── accessibility_map.html
│       └── accessibility_bar.png
├── NA_outputs/                 # Created after running network analysis
├── src/
│   └── park_accessibility/
│       ├── kd_park_accessibility/
│       └── NA_park_accessibility/
├── test/                       # Unit tests
├── pyproject.toml              # Project configuration
├── poetry.lock                 # Dependency lock file
└── README.md

⚙️ Installation & Setup

This project uses Poetry for dependency management.

1️⃣ Install dependencies
poetry install

2️⃣ Activate the virtual environment
poetry shell

▶️ Running the Analyses
▶ KD-Tree Accessibility Analysis
python main.py


This will generate outputs in:

outputs/KDoutput/

▶ Network-Based Accessibility Analysis
python NA_main.py

📊 Network Analysis Outputs

After running the network analysis, a folder named NA_outputs/ is created containing:

Spatial datasets

Amsterdam administrative boundary

Parks, buildings, and walking network

Stored as Shapefiles and GeoPackage (.gpkg) files

Visual outputs

Interactive accessibility maps (.html)

Static summary plots (.png)

Example:

NA_outputs/
├── amsterdam_boundary.gpkg
├── parks.gpkg
├── buildings.gpkg
├── walking_network.gpkg
├── amsterdam_park_accessibility.html
└── accessibility_summary.png

🌍 Viewing the Interactive Map

The interactive network-based accessibility map can be opened in a browser:

open NA_outputs/amsterdam_park_accessibility.html


The map allows users to explore:

Walking distance to the nearest park

Spatial disparities in park access

Neighborhood-level accessibility patterns

📈 Sample Results (Amsterdam – Network Analysis)
🏙 Data Overview

Total buildings: 197,057

Buildings with park access within 1500 m: 190,120

Buildings without park access within 1500 m: 6,937

📏 Distance Statistics (Walking Distance)

Minimum distance to nearest park: 0.0 m

Maximum distance to nearest park: 1,499.76 m

Mean distance to nearest park: 469.95 m

These results indicate that while most buildings have access to parks within walking distance, accessibility gaps remain, particularly at the urban periphery.

🌐 Web Visualization (GitHub Pages)

The generated HTML outputs are static and can be hosted directly using GitHub Pages.

Example URL:

https://<username>.github.io/<repository-name>/outputs/KDoutput/accessibility_map.html


This enables:

Easy sharing of results

Use in reports, applications, and presentations

No server or backend requirements

🧪 Testing

Unit tests ensure robustness of:

KD-Tree logic

Network computations

Geometric operations

Data downloading utilities

Run tests with:

pytest

🛠 Technologies Used

Python

GeoPandas

OSMnx

NetworkX

SciPy (KD-Tree)

Folium / Plotly

Poetry

PyTest

🔧 Development Notes

The KD-Tree and Network Analysis workflows were initially developed in separate Git branches to allow independent testing, optimization, and validation.
They were later merged into the main branch to provide a unified and reproducible accessibility analysis framework.
