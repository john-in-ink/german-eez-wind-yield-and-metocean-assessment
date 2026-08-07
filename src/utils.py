"""
German EEZ Wind Yield and Metocean Assessment - Master Engineering Utilities

Description: Unified mathematical production library consolidating boundary-layer aerodynamics,
             turbine power interpolation, metocean logistics, extreme value statistics,
             geotechnical scour, subsea finite gradients, and catenary mooring mechanics.
"""

import numpy as np
import config
from scipy.interpolate import interp1d
from scipy.stats import gumbel_r

# ==============================================================================
# 1. ATMOSPHERIC METEOROLOGY & WIND PROFILE MODEL
# ==============================================================================
def extrapolate_wind_speed(u_100m, v_100m, target_height=config.HUB_HEIGHT_M, baseline_height=100.0):
    """Applies the logarithmic wind profile law to extrapolate vectors to hub height."""
    wind_speed_100m = np.sqrt(u_100m**2 + v_100m**2)
    numerator = np.log(target_height / config.SURFACE_ROUGHNESS_OCEAN)
    denominator = np.log(baseline_height / config.SURFACE_ROUGHNESS_OCEAN)
    return wind_speed_100m * (numerator / denominator)

# ==============================================================================
# 2. TURBINE POWER INTERPOLATION ENGINE
# ==============================================================================
TURBINE_SPEED_POINTS = np.array([0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 25, 25.1, 40])
TURBINE_POWER_OUTPUTS = np.array([0, 0, 1.5, 3.0, 5.2, 7.8, 10.5, 12.8, 14.5, 15.0, 15.0, 0, 0])

_calculate_turbine_power = interp1d(
    TURBINE_SPEED_POINTS, TURBINE_POWER_OUTPUTS, 
    kind='linear', bounds_error=False, fill_value=0.0
)

def get_turbine_power_generation(wind_speeds_hub):
    """Maps continuous wind speed arrays directly to individual turbine output (MW)."""
    return _calculate_turbine_power(wind_speeds_hub)

# ==============================================================================
# 3. METOCEAN LOGISTICS & WAVE ACCESSIBILITY
# ==============================================================================
def model_significant_wave_height(wind_speeds_ms, seed=42):
    """Empirical metocean relationship mapping wind shear force to significant wave heights."""
    rng = np.random.default_rng(seed)
    wave_heights = (wind_speeds_ms * 0.22) + rng.normal(0.4, 0.3, len(wind_speeds_ms))
    return np.clip(wave_heights, 0.3, 8.5)

def evaluate_marine_accessibility(wave_heights_array):
    """Calculates percentage safety clearance windows for CTV and SOV maintenance vessels."""
    total_hours = len(wave_heights_array)
    if total_hours == 0: return 0.0, 0.0
    safe_ctv = np.sum(wave_heights_array <= 1.5)
    safe_sov = np.sum(wave_heights_array <= 2.5)
    return round((safe_ctv / total_hours) * 100, 1), round((safe_sov / total_hours) * 100, 1)

# ==============================================================================
# 4. EXTREME VALUE STATISTICS (RETURN METRICS)
# ==============================================================================
def fit_extreme_storm_h50(annual_max_waves, return_period_years=50):
    """Fits a Gumbel distribution to annual maxima to extrapolate design wave survival limits."""
    fitted_loc, fitted_scale = gumbel_r.fit(annual_max_waves)
    exceedance_prob = 1.0 / return_period_years
    design_threshold_h50 = gumbel_r.ppf(1.0 - exceedance_prob, loc=fitted_loc, scale=fitted_scale)
    return design_threshold_h50, fitted_loc, fitted_scale

# ==============================================================================
# 5. GEOTECHNICAL FOUNDATION SCOUR MITIGATION
# ==============================================================================
def design_monopile_scour_protection(monopile_diameter=10.0, rock_density=2650.0, rock_d50=0.45):
    """Computes equilibrium sand scour risk depth and designs rock apron material logistics."""
    equilibrium_scour_depth = 1.3 * monopile_diameter
    protection_radius = 4.5 * (monopile_diameter / 2)
    net_apron_area = (np.pi * (protection_radius**2)) - (np.pi * ((monopile_diameter / 2)**2))
    layer_thickness = 2.5 * rock_d50
    bulk_volume = net_apron_area * layer_thickness
    solid_mass_tonnes = (bulk_volume * (1 - 0.35) * rock_density) / 1000.0
    return equilibrium_scour_depth, bulk_volume, solid_mass_tonnes

# ==============================================================================
# 6. CENTRAL DIFFERENCE CABLE SLOPE GEOMETRY
# ==============================================================================
def analyze_cable_corridor_slopes(Z_corridor_matrix, spacing_m=1.0):
    """Computes localized terrain slope angles using spatial central differences."""
    dZ_dy, dZ_dx = np.gradient(Z_corridor_matrix, spacing_m)
    slope_magnitude = np.sqrt(dZ_dx**2 + dZ_dy**2)
    return np.arctan(slope_magnitude) * (180.0 / np.pi)

# ==============================================================================
# 7. DEEPWATER CATENARY MOORING MECHANICAL PROFILES
# ==============================================================================
def calculate_catenary_profile(T_h, weight_pm, depth=120.0):
    """Solves the hyperbolic cosine profile equations describing catenary line geometry."""
    a = T_h / weight_pm
    max_x = a * np.arccosh((depth + a) / a)
    x_coords = np.linspace(0, max_x, 100)
    z_coords = a * np.cosh(x_coords / a) - a
    return x_coords, z_coords

# ==============================================================================
# 8. ASSET MANAGEMENT & LIFECYCLE ECONOMICS
# ==============================================================================
def run_lifecycle_financial_model(net_annual_gwh, capacity_mw=15.0, years=25):
    """Evaluates CapEx, OpEx, asset payback windows, and overall project lifetime LCOE."""
    total_capex = capacity_mw * 3500000
    annual_opex = capacity_mw * 80000
    lifetime_mwh = (net_annual_gwh * 1000) * years
    lcoe_per_mwh = (total_capex + (annual_opex * years)) / lifetime_mwh
    annual_revenue = (net_annual_gwh * 1000) * 75.0
    payback_years = total_capex / (annual_revenue - annual_opex)
    return lcoe_per_mwh, payback_years
