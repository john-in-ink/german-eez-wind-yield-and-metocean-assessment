"""
German EEZ Wind Yield and Metocean Assessment - Master Orchestration Pipeline

Description: Primary driver script managing decoupled execution flow across 
             data acquisition, engineering analytics, and 7-panel dashboard plotting.
"""

import os
import sys
import logging

# Ensure root can seamlessly resolve imports inside the src namespace directory
sys.path.append(os.path.abspath("src"))

import config
from download_metocean_data import download_era5_metocean_data
from analytics import run_production_pipeline
from plots import generate_all_seven_plots

# Configure professional enterprise logging framework
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)


def main():
    """Orchestrates end-to-end execution of the offshore asset evaluation suite."""
    logger.info("==================================================================")
    logger.info("   STARTING MASTER DECOUPLED OFFSHORE WIND PIPELINE DRIVER")
    logger.info("==================================================================")

    # --------------------------------------------------------------------------
    # STEP 1: DECOUPLED DATA ACQUISITION LAYER
    # --------------------------------------------------------------------------
    if not os.path.exists(config.RAW_DATA_FILE):
        logger.warning(f"Data layer empty. Target file not found at path: {config.RAW_DATA_FILE}")
        logger.info("Launching isolated Data Acquisition Pipeline (January 2025 Query Mode)...")
        
        # Ensure data infrastructure directory folder path exists on disk
        os.makedirs(os.path.dirname(config.RAW_DATA_FILE), exist_ok=True)
        download_era5_metocean_data(output_path=config.RAW_DATA_FILE)
        
        logger.info("Data Acquisition Phase successfully completed.")
    else:
        logger.info(f"Verified immutable raw dataset cache on disk at: {config.RAW_DATA_FILE}")

    # --------------------------------------------------------------------------
    # STEP 2: METOCEAN PHYSICS & FINANCIAL ANALYTICS LAYER
    # --------------------------------------------------------------------------
    logger.info("Transitioning control to Engineering Analytics Engine...")
    metrics_csv_path = run_production_pipeline()
    logger.info("Analytical physics and commercial report compiling completed.")

    # --------------------------------------------------------------------------
    # STEP 3: MASTER VISUAL AUDIT GENERATION LAYER (ALL 7 REQUIRED FIGURES)
    # --------------------------------------------------------------------------
    logger.info("Transitioning control to Master Visualization Engine...")
    generate_all_seven_plots(metrics_csv_path)
    logger.info("Engineering graphic asset production pipeline completed.")

    logger.info("==================================================================")
    logger.info("   END-TO-END PIPELINE SYSTEM COMPLETION SUCCESSFUL")
    logger.info("==================================================================")


if __name__ == "__main__":
    main()
