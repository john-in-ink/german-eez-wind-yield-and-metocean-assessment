# German EEZ Offshore Wind Yield and Metocean Engineering Assessment

**Asset Array:** 630 MW Deepwater Array with 42 x 15MW Reference Nodes
**Geographic Domain:** German EEZ, North Sea Bight
**Regulatory Design Baselines:** BSH Standards

An end-to-end site suitability and yield assessment suite bridging multi-dimensional atmospheric and oceanography reanalysis datasets with bankable project financials. This repository serves as a professional portfolio project demonstrating advanced production capabilities in Wind Resource Assessment, Metocean Engineering, and Asset Optimization Architecture.

---

## Consolidated Asset Performance Indicators (KPIs)

The main execution pipeline programmatically generates the following core performance matrix for the target deployment node:

- Gross Generation Potential: 1,514.86 GWh per year (Theoretical continuous power curve output before wake and electrical drag)
- Cumulative System Deficit: 17.0 % (Piecewise engineering deduction factoring arrays, wakes, and downtime loops)
- True Commercial Net Yield: 1,257.33 GWh per year (Bankable production volume expected at the onshore transformation node)
- Net Farm Capacity Factor: 54.4 % (Macro-scale asset performance classification reflecting deepwater arrays)
- Levelized Cost of Energy: 48.24 Euros per MWh (Competitive operational LCOE baseline optimized to North Sea thresholds)
- Asset Payback Period: 6.4 Years (Capital amortization horizon based on standard market valuation assumptions)

---

## Key Analytical Engineering Modules

### 1. Data Acquisition Pipeline (src/download_metocean_data.py)
Automated Climate Downloads: Handles the systematic download of historical ERA5 climate reanalysis datasets directly from the Copernicus Climate Data Store. It pulls multi-component wind velocity data and wave parameters across a geofenced North Sea marine cluster bounding box.

### 2. Atmospheric Boundary Layer Physics and Aerodynamics (src/utils.py)
- Logarithmic Extrapolation: Scales raw Copernicus multi-component velocity vectors from the 100m reference standard up to the target 150m hub height using the Log Wind Profile law, parameterized for open-sea roughness paths.
- Quadratic Spline Coupling: Passes continuous hub velocity records into a localized high-order mathematical power curve array. Transitioning from coarse linear mapping to quadratic interpolation prevents artificial energy overestimations during the critical wind speed ramp-up window from 3.0 to 11.0 m per second.

### 3. Metocean Transport Logistics and Marine Accessibility
- Wave Shear Modeling: Generates correlated multi-year time-series significant wave heights using an empirical fluid shear stress framework linked directly to kinetic wind gradients.
- Vessel Operating Windows: Computes exact safe transfer capabilities across the calendar year. Establishes that standard Crew Transfer Vessels achieve 71.2% operational clearance, while heavy Walk-to-Work Service Operation Vessels expand access windows to 93.8%.

### 4. Extreme Value Statistics and Survival Limits
- Gumbel Distribution Fitting: Extracts annual hydrographic maxima to fit extreme value right-skewed parametric boundaries.
- 50-Year Design Limits: Extrapolates the critical 50-year return period significant wave height threshold to establish explicit structural Ultimate Limit State baselines for floating platform survivability.

### 5. Marine Geotechnical and Layout Mechanics
- Subsea Gradient Analysis: Applies spatial central differences across a digital elevation matrix to calculate local seafloor slope gradients, automatically flagging cable burial plow geometric hazard alerts.
- Catenary Mooring Profiles: Solves hyperbolic cosine static equilibrium mechanics to accurately chart mooring line tension profiles and platform station-keeping limits under subsea deadweight stresses.

---

## Production Repository Topology

german-eez-wind-yield-and-metocean-assessment/
├── LICENSE                     # MIT License specification text
├── requirements.txt            # Explicit dependency version locks
├── README.md                   # Primary portfolio documentation page
├── data/
│   └── north_sea_metocean_raw.nc # Downloaded raw NetCDF spatial array file
├── notebooks/
│   └── yield_and_metocean_plots.ipynb  # Verification visualizations and analytical plots
├── outputs/
│   ├── german_bight_asset_yield_metrics.csv  # Sliced engineering flat files
│   └── EXECUTIVE_YIELD_REPORT.md             # Pipeline-generated briefing report
└── src/
    ├── __init__.py             # Namespace declaration
    ├── analytics.py            # Primary pipeline execution engine
    ├── config.py               # Centralized site configurations and constants
    ├── download_metocean_data.py # Automated CDS reanalysis data download script
    └── utils.py                # Core engineering mathematical library

---

## Environment Provisioning and Pipeline Execution

This project is built using Python 3.10+ and depends on production-grade geospatial and scientific data libraries. Follow these steps to spin up the asset matrix locally:

### 1. Initialize Virtual Environment and Dependencies
Run these setup commands in your terminal application:
cd german-eez-wind-yield-and-metocean-assessment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 2. Configure Credentials and Execute Data Pipelines
Set up your system environment tokens for the Copernicus Climate Data Store interface, run data ingestion, and then fire the analytical matrix scripts:
export CDSAPI_URL="your_url_here"
export CDSAPI_KEY="your_private_uid_and_key_here"

python src/download_metocean_data.py
python src/analytics.py

Upon successful execution, the pipeline will log progress directly to the terminal console, export a clean data structure to your data folder, and write an updated report file.

---

## License
This project is open-source software licensed under the MIT License.
