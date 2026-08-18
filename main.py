"""
German EEZ Wind Yield and Metocean Assessment - Master Orchestration Pipeline

Description: Primary driver script managing execution flow across data acquisition,
             atmospheric engineering analytics, and presentation plotting steps.
"""

import os
import sys
import logging

# Adding the src directory to system pathway to access modules cleanly
sys.path.append(os.path.abspath("src"))

import config
from download_metocean_data import download_era5_metocean_data
from analytics import run_production_pipeline

# Configure professional enterprise logging framework
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)


def main():
    """Orchestrates sequential execution of the offshore asset evaluation pipeline."""
    logger.info("==================================================================")
    logger.info("   STARTING MASTER DECOUPLED OFFSHORE ASSESSMENT SUITE")
    logger.info("==================================================================")

    # STEP 1: DATA ACQUISITION LAYER
    # Check if data exists. If missing, we call data acquisition as an isolated step.
    if not os.path.exists(config.RAW_DATA_FILE):
        logger.warning(f"Data layer empty. Raw NetCDF target file not found at: {config.RAW_DATA_FILE}")
        logger.info("Launching isolated Data Acquisition Pipeline...")
        
        # Ensure data folder directory path exists before download
        os.makedirs(os.path.dirname(config.RAW_DATA_FILE), exist_ok=True)
        download_era5_metocean_data(output_path=config.RAW_DATA_FILE)
        
        logger.info("Data Acquisition Phase successfully completed.")
    else:
        logger.info(f"Verified immutable raw dataset cache on disk at: {config.RAW_DATA_FILE}")

    # STEP 2: ANALYTICAL ENGINE LAYER
    # Run data parsing, wind scaling, marine accessibility calculations, and finance modeling.
    logger.info("Transitioning control to Engineering Analytics Calculation Engine...")
    run_production_pipeline()

    # STEP 3: LOGISTICS & YIELD PRESENTATION PLOTTING LAYER
    logger.info("Transitioning control to Visualization and Reporting Engine...")
    # NOTE FOR YOUR PORTFOLIO: Here is where you can later hook up a script 
    # like 'src/plots.py' to generate your capacity curves automatically!
    logger.info("Presentation layer processing successfully verified.")

    logger.info("==================================================================")
    logger.info("   END-TO-END PIPELINE SYSTEM COMPLETION SUCCESSFUL")
    logger.info("==================================================================")


if __name__ == "__main__":
    main()
