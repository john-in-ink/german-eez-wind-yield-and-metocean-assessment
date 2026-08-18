"""
German EEZ Wind Yield and Metocean Assessment - Analytics Execution Pipeline

Description: Master script orchestrating the scientific ingestion of Copernicus NetCDF data,
             executing metocean physics models, engineering asset power curves, and 
             exporting production matrices for commercial asset reporting.
"""

import os
import sys
import logging
import xarray as xr
import pandas as pd
import numpy as np

# Import our custom engineering modules
import config
import utils

# Configure professional enterprise logging framework
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def run_production_pipeline() -> str:
    """
    Executes the end-to-end yield and metocean assessment analytics engine.
    """
    print("\n" + "="*60)
    print("   LAUNCHING GERMAN EEZ ASSET ANALYTICS PIPELINE")
    print("="*60)
    
    # 1. Direct, clear raw data existence check boundary
    if not os.path.exists(config.RAW_DATA_FILE):
        print(f"[ERROR] Raw data file not found: {config.RAW_DATA_FILE}")
        sys.exit(1)
        
    print(f"[INFO] Ingesting multi-dimensional spatial grid: {config.RAW_DATA_FILE}")
    ds = xr.open_dataset(config.RAW_DATA_FILE)
    
    # 2. Localized Spatial Slicing (Isolating the primary asset development point)
    target_lat = float(ds['latitude'].values[0] if ds['latitude'].ndim > 0 else ds['latitude'].values)
    target_lon = float(ds['longitude'].values[0] if ds['longitude'].ndim > 0 else ds['longitude'].values)
    print(f"[INFO] Geofencing asset location coordinate: {target_lat}°N, {target_lon}°E")
    
    # Slice the multi-dimensional dataset to prevent memory bloat
    site_ds = ds.sel(latitude=target_lat, longitude=target_lon, method='nearest')
    
    # 3. Convert sliced spatial node to a localized production dataframe
    print("[INFO] Unpacking multidimensional matrix into standard time-series matrix...")
    site_df = site_ds.to_dataframe().reset_index()
    
    # Standardize column mappings from Copernicus ERA5 keys
    time_col = 'valid_time' if 'valid_time' in site_df.columns else 'time'
    u_col = 'u100' if 'u100' in site_df.columns else '100m_u_component_of_wind'
    v_col = 'v100' if 'v100' in site_df.columns else '100m_v_component_of_wind'
    
    site_df = site_df.rename(columns={time_col: 'Timestamp'})
    
    # 4. Wind Profile Extrapolation & Power Coupling via utils library
    print("[INFO] Processing boundary layer wind logs up to 150m hub height...")
    site_df['Wind_Speed_Hub_ms'] = utils.extrapolate_wind_speed(site_df[u_col], site_df[v_col])
    
    print("[INFO] Executing turbine power curve interpolation engine...")
    site_df['Turbine_Power_MW'] = utils.get_turbine_power_generation(site_df['Wind_Speed_Hub_ms'])
    
    # Scale up to a full utility-scale 42-turbine deployment matrix
    total_turbines = 42
    site_df['Farm_Gross_Power_MW'] = site_df['Turbine_Power_MW'] * total_turbines
    
    # 5. Calculate Consolidated Metocean Yield & Accessibility Summaries
    print("[INFO] Evaluating wind farm localized performance indicators...")
    hourly_winds = site_df['Wind_Speed_Hub_ms'].values
    
    # Universal timeframe adaptation: Dynamically query total hours available from the dataset
    simulated_hours = len(site_df)
    
    gross_theoretical_gwh = (site_df['Farm_Gross_Power_MW'].sum()) / 1000.0
    cumulative_loss_pct = 17.0  # 17% industrial loss penalty baseline
    net_energy_to_grid_gwh = gross_theoretical_gwh * (1.0 - (cumulative_loss_pct / 100.0))
    
    # Dynamic capacity factor divisor calculation based on dataset size
    max_theoretical_energy_gwh = (total_turbines * 15.0 * simulated_hours) / 1000.0
    net_capacity_factor_pct = (net_energy_to_grid_gwh / max_theoretical_energy_gwh) * 100.0 if max_theoretical_energy_gwh > 0 else 0.0
    
    # Generate matched wave profiles using our empirical metocean relationship
    print("[INFO] Modeling localized significant wave conditions...")
    site_df['Modeled_Hs_m'] = utils.model_significant_wave_height(site_df['Wind_Speed_Hub_ms'].values)
    
    ctv_acc, sov_acc = utils.evaluate_marine_accessibility(site_df['Modeled_Hs_m'].values)
    
    # 6. Execute Lifecycle Financial Projections
    print("[INFO] Running structural asset economics and payback simulations...")
    lcoe, payback_period = utils.run_lifecycle_financial_model(net_energy_to_grid_gwh / total_turbines)
    
    # 7. Print Master Summary directly to terminal screen
    print("\n" + "="*60)
    print("   PRODUCTION ENGINEERING & ASSET YIELD ASSESSMENT")
    print("="*60)
    print(f"Operational Scope:         {simulated_hours} Hours Analyzed")
    print(f"Mean Wind Speed at Hub:    {site_df['Wind_Speed_Hub_ms'].mean():.2f} m/s")
    print(f"Gross Farm Generation:     {gross_theoretical_gwh:.2f} GWh")
    print(f"Industrial Loss Penalty:   {cumulative_loss_pct:.1f} %")
    print(f"Net Energy to Grid:        {net_energy_to_grid_gwh:.2f} GWh")
    print(f"Net Asset Capacity Factor: {net_capacity_factor_pct:.1f} %")
    print("-"*60)
    print("   LOGISTICS & METOCEAN ACCESSIBILITY WINDOWS")
    print("-"*60)
    print(f"CTV Access (Hs <= 1.5m):   {ctv_acc:.1f}% of data scope")
    print(f"SOV Access (Hs <= 2.5m):   {sov_acc:.1f}% of data scope")
    print("-"*60)
    print("   COMMERCIAL LIFE-CYCLE FINANCIAL ASSESSMENT")
    print("-"*60)
    print(f"Project Lifetime LCOE:     €{lcoe:.2f} per MWh")
    print(f"Estimated Asset Payback:   {payback_period:.1f} Years")
    print("="*60)
    
    # 8. Export clean production data tables to disk
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)
    output_csv = os.path.join(config.OUTPUT_DIR, "german_bight_asset_yield_metrics.csv")
    print(f"[SUCCESS] Exporting production flat data matrix to: {output_csv}")
    
    columns_to_export = ['Timestamp', 'Wind_Speed_Hub_ms', 'Turbine_Power_MW', 'Farm_Gross_Power_MW', 'Modeled_Hs_m']
    site_df[columns_to_export].to_csv(output_csv, index=False)
    print("Pipeline Execution Completed Successfully.\n")
    
    return output_csv

if __name__ == "__main__":
    run_production_pipeline()
