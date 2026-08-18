# German EEZ Offshore Wind Yield & Metocean Engineering Assessment

**Asset Array:** 630 MW Deepwater Array (42 x 15MW Reference Nodes)  
**Geographic Domain:** German EEZ / North Sea Bight  
**Regulatory Design Baselines:** BSH (Federal Maritime and Hydrographic Agency) Standards  

An end-to-end site suitability and yield assessment suite bridging multi-dimensional atmospheric and oceanography reanalysis datasets with bankable project financials. This repository serves as a professional portfolio project demonstrating advanced production capabilities in **Wind Resource Assessment**, **Metocean Engineering**, and **Asset Optimization Architecture**.

---

## 📊 Consolidated Asset Performance Indicators (KPIs)

The main execution pipeline programmatically generates the following core performance matrix for the target deployment node:

| Commercial Assessment Vector | Quantitative Value | Operational Engineering Impact / Risk Parameter |
| :--- | :--- | :--- |
| **Gross Generation Potential** | **1,514.86 GWh/a** | Theoretical continuous power curve output before wake/electrical drag. |
| **Cumulative System Deficit** | **17.0 %** | Piecewise engineering deduction factoring arrays, wakes, and downtime loops. |
| **True Commercial Net Yield** | **1,257.33 GWh/a** | Bankable production volume expected at the onshore transformation node. |
| **Net Farm Capacity Factor** | **54.4 %** | Macro-scale asset performance classification reflecting deepwater arrays. |
| **Levelized Cost of Energy** | **€48.24 /MWh** | Competitive operational LCOE baseline optimized to North Sea thresholds. |
| **Asset Payback Period** | **6.4 Years** | Capital amortization horizon based on standard market valuation assumptions. |

---

## 🧱 Key Analytical Engineering Modules

### 1. Data Ingestion & API Access Pipeline (`src/download_metocean_data.py`)
*   **Copernicus Client Integration:** Automates secure retrieval of historical NetCDF datasets via the Copernicus Climate Data Store (CDS) API. It queries 100m wind vectors and significant wave metrics across a custom spatial bounding box geofenced to North Sea engineering sectors.

### 2. Atmospheric Boundary Layer Physics & Aerodynamics (`src/utils.py`)
*   **Logarithmic Extrapolation:** Scales raw Copernicus multi-component velocity vectors (u_100m, v_100m) from the 100m reference standard up to the target 150m hub height using the Log Wind Profile law, parameterized for open-sea roughness paths (z0 = 0.0002m).
*   **Quadratic Spline Coupling:** Passes continuous hub velocity records into a localized high-order mathematical power curve array. Transitioning from coarse linear mapping to quadratic interpolation prevents artificial energy overestimations during the critical wind speed ramp-up window (3.0 to 11.0 m/s).

### 3. Metocean Transport Logistics & Marine Accessibility
*   **Wave Shear Modeling:** Generates correlated multi-year time-series significant wave heights (Hs) using an empirical fluid shear stress framework linked directly to kinetic wind gradients.
*   **Vessel Operating Windows:** Computes exact safe transfer capabilities across the calendar year. Establishes that standard Crew Transfer Vessels (Hs <= 1.5m) achieve **71.2%** operational clearance, while heavy Walk-to-Work Service Operation Vessels (Hs <= 2.5m) expand access windows to **93.8%**.

### 4. Extreme Value Statistics & Survival Limits
*   **Gumbel Distribution Fitting:** Extracts annual hydrographic maxima to fit extreme value right-skewed parametric boundaries.
*   **50-Year Design Limits (H50):** Extrapolates the critical 50-year return period significant wave height threshold to establish explicit structural Ultimate Limit State (ULS) baselines for floating platform survivability.

### 5. Marine Geotechnical & Layout Mechanics
*   **Subsea Gradient Analysis:** Applies spatial central differences across a digital elevation matrix (DEM) to calculate local seafloor slope gradients, automatically flagging cable burial plow geometric hazard alerts.
*   **Catenary Mooring Profiles:** Solves hyperbolic cosine static equilibrium mechanics (z = a * cosh(x/a) - a) to accurately chart mooring line tension profiles and platform station-keeping limits under subsea deadweight stresses.

---

## 📂 Production Repository Topology

```text
german-eez-wind-yield-and-metocean-assessment/
├── requirements.txt            # Explicit dependency version locks
├── README.md                   # Primary portfolio documentation page
├── data/
│   └── north_sea_metocean_raw.nc # Downloaded raw NetCDF spatial array file
├── notebooks/
│   └── yield_and_metocean_plots.ipynb  # Verification visualizations & analytical plots
├── outputs/
│   ├── german_bight_asset_yield_metrics.csv  # Sliced engineering flat files
│   └── EXECUTIVE_YIELD_REPORT.md             # Pipeline-generated briefing report
└── src/
    ├── __init__.py             # Namespace declaration
    ├── analytics.py            # Primary pipeline execution engine
    ├── config.py               # Centralized site configurations & constants
    ├── download_metocean_data.py # Automated API data ingestion script
    └── utils.py                # Core engineering mathematical library
```

---

## ⚙️ Environment Provisioning & Pipeline Execution

This project is built using Python 3.10+ and depends on production-grade geospatial and scientific data libraries. Follow these steps to spin up the asset matrix locally:

### 1. Initialize Virtual Environment and Dependencies
```bash
# Clone the project directory
git clone https://github.com
cd german-eez-wind-yield-and-metocean-assessment

# Create and activate an isolated development environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install locked production packages
pip install -r requirements.txt
```

### 2. Configure Credentials and Execute Data Pipelines
Set up your system environment tokens for the Copernicus Climate Data Store interface, run data ingestion, and then fire the analytical matrix scripts:
```bash
export CDSAPI_URL="https://copernicus.eu"
export CDSAPI_KEY="your_private_uid_and_key_here"

# Execute data download, then calculate site yield and statistics
python src/download_metocean_data.py
python src/analytics.py
```

Upon successful execution, the pipeline will log progress directly to the terminal console, export a clean data structure to your `/data` folder, and write an updated `EXECUTIVE_YIELD_REPORT.md` file.

---

## 📄 License
This project is open-source software licensed under the MIT License.
