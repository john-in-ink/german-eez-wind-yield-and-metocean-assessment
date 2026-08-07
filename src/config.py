"""
German EEZ Wind Yield and Metocean Assessment - Configuration Parameters

Description: Centralized engineering, financial, and environmental constants 
             modeled for utility-scale offshore wind assets in the German Bight.
"""

import os

# ==============================================================================
# 1. GEOGRAPHIC & ENVIRONMENTAL BOUNDARIES
# ==============================================================================
# Regulated boundaries matching the BSH (Bundesamt für Seeschifffahrt und Hydrographie)
DATA_DIR = "data"
OUTPUT_DIR = "outputs"
RAW_DATA_FILE = os.path.join(DATA_DIR, "german_bight_metocean_raw.nc")

LAT_NORTH = 56.0
LAT_SOUTH = 53.3
LON_WEST = 6.0
LON_EAST = 9.0

# ==============================================================================
# 2. TURBINE TECHNICAL CONFIGURATION (Reference: Generic 15MW Offshore Turbine)
# ==============================================================================
# Modeled closely on standard offshore reference designs used by Siemens Gamesa / Vestas
HUB_HEIGHT_M = 150.0        # Industry standard height for modern 15MW-20MW assets
ROTOR_DIAMETER_M = 236.0    # Swept area calculations
RATED_CAPACITY_MW = 15.0    # Individual turbine nominal rating
CUT_IN_SPEED_MS = 3.0       # Wind speed where power production initiates
RATED_SPEED_MS = 11.0       # Wind speed where turbine reaches max capacity
CUT_OUT_SPEED_MS = 25.0     # Maximum survival speed before safety shutdown

# Surface roughness length (z0) for open ocean with fully developed waves
SURFACE_ROUGHNESS_OCEAN = 0.0002  

# ==============================================================================
# 3. COMMERCIAL LOSS FACTOR METRICS
# ==============================================================================
# Replicating the 17.0% cumulative energy deficit shown in your layout analytics
LOSS_FACTORS = {
    "wake_losses": 0.08,        # Internal and neighboring farm wake degradation (8%)
    "electrical_losses": 0.03,  # Array cable and offshore substation transmission resistance (3%)
    "availability_losses": 0.04,# Scheduled maintenance and environmental downtime shutdowns (4%)
    "environmental_losses": 0.02 # Blade degradation, icing, and marine fouling (2%)
}

# Calculated total efficiency coefficient remaining (Multiplying out the remaining energy)
# (1 - 0.08) * (1 - 0.03) * (1 - 0.04) * (1 - 0.02) = ~0.839 (approx. 16.1% to 17% loss)

