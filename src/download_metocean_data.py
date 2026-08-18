"""
German EEZ North Sea Metocean and Wind Yield Assessment - Data Acquisition Pipeline

Description: Automates the retrieval of ERA5 climate reanalysis datasets 
             (wind velocity components and wave height parameters) using the 
             Copernicus Climate Data Store (CDS) API.

Target Domain: German Exclusive Economic Zone (EEZ) / Deutsche Bucht [56.0, 6.0, 53.3, 9.0]
"""


import os
import sys
import cdsapi

def get_api_client():
    """
    Initializes the Copernicus CDS API client.
    (Ensures credentials are professionally handled via system environment variables)
    """
    # Check if user has set up their credentials correctly
    if not os.environ.get("CDSAPI_URL") or not os.environ.get("CDSAPI_KEY"):
        print("[ERROR] Copernicus CDS API credentials not found in environment variables.")
        print("Please export CDSAPI_URL and CDSAPI_KEY before running this script.")
        sys.exit(1)
        
    return cdsapi.Client()

def download_era5_metocean_data(output_path="data/german_bight_metocean_raw.nc"):
    """
    Requests and downloads wind and wave datasets for the specified North Sea bounding box.
    """
    c = get_api_client()
    
    print(f"[INFO] Initiating request to Copernicus CDS for North Sea datasets...")
    
    # German North Sea offshore wind cluster bounding box: [North, West, South, East]
    north_sea_bounds = [60.0, -4.0, 50.0, 10.0]
    
    try:
        c.retrieve(
            'reanalysis-era5-single-levels',
            {
                'product_type': 'reanalysis',
                'format': 'netcdf',
                # 100m --- ~hub height
                'variable': [
                    '100m_u_component_of_wind', 
                    '100m_v_component_of_wind',
                    'significant_height_of_combined_wind_waves_and_swell',
                    'mean_wave_period'
                ],
                'year': ['2025'],
                'month': ['01'],
                'day': [f"{i:02d}" for i in range(1, 31 + 1)],
                'time': [f"{i:02d}:00" for i in range(0, 24)],
                'area': north_sea_bounds,
            },
            output_path
        )
        print(f"[SUCCESS] Dataset successfully saved to: {output_path}")
        
    except Exception as e:
        print(f"[ERROR] Failed to retrieve data from Copernicus API: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Ensure the script executes properly when called directly from the command line
    download_era5_metocean_data()
