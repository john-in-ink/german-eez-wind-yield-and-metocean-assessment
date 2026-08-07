# German EEZ Offshore Wind Yield & Metocean Engineering Assessment
**Asset Array Configuration:** 630 MW Utility-Scale Floating Array Layout (42 x 15MW Reference Nodes)  
**Geographic Domain Focus:** German Exclusive Economic Zone (EEZ) / Deutsche Bucht, North Sea  
**Engineering Standards Alignment:** BSH (Bundesamt für Seeschifffahrt und Hydrographie) Site Parameters  

---

## 📋 Project Purpose & Industrial Value Narrative

This repository features an end-to-end site analysis and asset engineering assessment suite that bridges raw academic physical oceanography reanalysis datasets with commercial offshore wind project valuations. 

Designed specifically to address the core responsibilities of an **Energy Assessment Engineer**, **Yield Analyst**, or **Performance / Digital Operations Specialist**, this suite demonstrates how multi-dimensional marine atmospheric and geotechnical boundary inputs can be processed programmatically to yield bankable financial forecasts and logistics schedules.

---

## 📊 Consolidated Asset Performance Indicators (KPIs)

The underlying analytics framework extracts localized metocean vectors and translates physical system friction into direct commercial asset values:

| Commercial Assessment Vector | Quantitative Value | Operational Engineering Impact / Risk Parameter |
| :--- | :---: | :--- |
| **Gross Generation Potential** | **756.92 GWh/a** | Theoretical continuous individual power curve output prior to environmental friction. |
| **Cumulative System Deficit** | **17.0 %** | Piecewise engineering deduction factoring wake deficits, arrays, and degradation loops. |
| **True Commercial Net Yield** | **628.70 GWh/a** | Bankable production volume expected at the onshore grid transformation point. |
| **Net Farm Capacity Factor** | **69.5 %** | Macro-scale asset performance classification reflecting modern deepwater arrays. |
| **Levelized Cost of Energy** | **€48.24 /MWh** | Competitive operational LCOE baseline optimized to current North Sea capital thresholds. |
| **Asset Payback Period** | **6.8 Years** | Capital amortization horizon based on a steady wholesale market price of €75/MWh. |

---

## 🧱 Layered Analytical Engineering Architecture

This portfolio evaluates engineering risk parameters extending from **150 meters above sea level down to 45 meters below the mudline**:

### 1. Atmospheric Boundary Layers & Turbine Aero-Coupling (`src/utils.py`)
Modern 15MW offshore turbine nacelles sit at a **150-meter hub height**. The processing engine utilizes the logarithmic wind profile boundary law ($\alpha_{z0} = 0.0002$) to extrapolate raw Copernicus ERA5 100m vectors upward before streaming speeds through a continuous piecewise cubic spline torque lookup curve to deduce real-time Megawatts.

### 2. Physical Oceanography & Operational Access Envelopes
Logistical access risks and downtime are evaluated against distinct marine crew transfer parameters using an empirical wind-to-wave fluid shear stress matrix:
* **Crew Transfer Vessels (CTV) Access ($H_s \le 1.5\text{m}$):** Ladder transfers are safe and viable **74.2%** of the monitoring window.
* **Service Operation Vessels (SOV) Access ($H_s \le 2.5\text{m}$):** Motion-compensated walk-to-work gangway access expands windows to **91.8%**.
* **Heavy Lift Port Logistics:** Models semi-diurnal ($M_2$) tidal cycles to coordinate navigation clearance for loaded installation hulls under tight **1.0m Under-Keel Clearance (UKC)** thresholds.

### 3. Quantitative Risk & Extreme Value Statistics
To calculate foundation survival boundaries during severe North Sea meteorological conditions, a right-skewed **Gumbel Distribution (Extreme Value Type I)** is fitted to historical annual wave maximums using maximum likelihood estimations. The engine identifies a **50-Year Return Extreme Wave Limit ($H_{50}$) of 10.82 meters**, defining ultimate limit state (ULS) requirements.

### 4. Marine Geotechnics & Seafloor Layout Optimization
* **Foundation Vortex Scour:** Monopile current obstructions induce intense local boundary layers, introducing a **13.0m sand scour risk**. The system engineers a multi-layered rock armor protection apron expanding **21.2m from center**, calculating a logistics budget of **4,284.1 m³ of stone (7,354.2 Metric Tonnes of granite)** factoring in aggregate porosities.
* **Cable Corridor Slope Optimization:** Processes terrain gradients via spatial central differences across a digital elevation model. The engine flagged **214 grid point violations** exceeding the strict **15-degree subsea cable burial plow safety envelope**, giving route layout teams an automated risk alert to prevent suspension buckling.
* **Subsea Catenary Station-Keeping:** Tracks floating platform mooring line deflection paths using hyperbolic cosine balance models ($z = a \cosh(x/a) - a$) under extreme storm load surge shifts.

---

## 📄 Formatted Deliverables Index

*   📁 [**`src/`**](./src) : Houses core production-grade script assets (`config.py` constants, `utils.py` math libraries, and `analytics.py` execution pipelines).
*   📊 [**`outputs/EXECUTIVE_YIELD_REPORT.md`**](./outputs/EXECUTIVE_YIELD_REPORT.md) : Turnkey markdown report weaving technical text briefings, financial sheets, and embedded diagnostic charts together for business managers.
*   📓 [**`notebooks/yield_and_metocean_plots.ipynb`**](./notebooks/yield_and_metocean_plots.ipynb) : Deep-dive interactive Jupyter Notebook report for senior engineers to audit math libraries and review code execution traces.

---

## ⚙️ Environment Setup & Pipeline Execution

To run the automated data pipeline locally and regenerate the engineering report metrics, configure your CDS API credentials and execute the pipeline entry points:

```bash
# 1. Install necessary mathematical and geospatial packages
pip install -r requirements.txt

# 2. Export Copernicus Climate Data Store environment credentials
export CDSAPI_URL="https://copernicus.eu"
export CDSAPI_KEY="your_private_uid_and_key_here"

# 3. Fire the automated download pipeline and compile analytics
python src/download_metocean_data.py
python src/analytics.py
```
