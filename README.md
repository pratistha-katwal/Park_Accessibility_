
# 🌳 Park Accessibility Analysis: KD-Tree vs Network Analysis

A comprehensive Python toolkit for evaluating urban park accessibility using two complementary spatial approaches: **KD-Tree-based Euclidean distance** and **network-based walking distance** analysis. This project generates static, reproducible outputs suitable for web hosting and urban planning applications.

## 📋 Overview

Urban green spaces are crucial for public health, climate resilience, and environmental equity. This project provides methods to quantify and visualize park accessibility at the building level, enabling comparisons between simplified Euclidean distances and realistic walking routes.

## 🧠 Methodological Approaches

### 1️⃣ **KD-Tree-Based Accessibility (Euclidean Distance)**
**Objective:** Fast nearest-park identification using straight-line distances.
- **Advantages:** Extremely fast, scales well to city-level datasets
- **Limitations:** Doesn't account for street networks or barriers
- **Best for:** Exploratory analysis and comparative studies

### 2️⃣ **Network-Based Accessibility (Walking Distance)**
**Objective:** Realistic walking accessibility using pedestrian street networks.
- **Advantages:** Accounts for street connectivity and real walking routes
- **Limitations:** Computationally more expensive
- **Best for:** Planning, policy applications, and detailed assessments

## 📂 Repository Structure

```
├── main.py                     # Entry point for KD-Tree workflow
├── NA_main.py                  # Entry point for Network Analysis workflow
├── outputs/
│   └── KDoutput/
│       ├── accessibility_map.html
│       └── accessibility_bar.png
├── NA_outputs/                 # Created after running network analysis
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
├── test/                       # Unit tests
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
git clone <repository-url>
cd park-accessibility-analysis
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
python NA_main.py
```
**Outputs:** Generated in `NA_outputs/` (created automatically)
- Spatial datasets (GeoPackage format)
- Interactive accessibility maps (.html)
- Static summary plots (.png)

## 📊 Sample Results (Amsterdam - Network Analysis)

### 🏙 **Data Overview**
- Total buildings: 197,057
- Buildings with park access within 1500 m: 190,120 (96.5%)
- Buildings without park access within 1500 m: 6,937 (3.5%)

### 📏 **Distance Statistics (Walking Distance)**
- Minimum distance to nearest park: 0.0 m
- Maximum distance to nearest park: 1,499.76 m
- Mean distance to nearest park: 469.95 m

## 🌍 Viewing Interactive Maps

### Local Viewing
```bash
# KD-Tree results
open outputs/KDoutput/accessibility_map.html

# Network Analysis results
open NA_outputs/amsterdam_park_accessibility.html
```

### Web Hosting via GitHub Pages
The generated HTML outputs are static and can be hosted directly using GitHub Pages:

1. Enable GitHub Pages in repository settings
2. Set source to `/docs` folder or root directory
3. Access via: `https://<username>.github.io/<repository-name>/outputs/KDoutput/accessibility_map.html`

## 🧪 Testing

Run unit tests to ensure robustness:
```bash
pytest
```

Tests cover:
- KD-Tree logic and queries
- Network computations
- Geometric operations
- Data downloading utilities

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

## 🔧 Development Notes

- **Branch History:** The KD-Tree and Network Analysis workflows were developed in separate Git branches for independent testing and optimization before merging into the main branch.
- **Reproducibility:** All outputs are static and deterministic, ensuring reproducible results across runs.
- **Scalability:** Both methods are designed to scale from neighborhood to city-level analysis.

## 📈 Applications & Use Cases

- **Urban Planning:** Identify accessibility gaps and prioritize park development
- **Public Health:** Correlate park access with health outcomes
- **Environmental Justice:** Assess equitable distribution of green spaces
- **Real Estate:** Evaluate neighborhood amenities
- **Academic Research:** Comparative spatial analysis methodologies

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## 📄 License

[Specify your license here]

## 📧 Contact

[Your name/organization contact information]

---

*This project enables evidence-based decision making for urban green space planning through robust spatial analysis and accessible visualizations.*
```
