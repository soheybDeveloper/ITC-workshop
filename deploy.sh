#!/bin/bash

# Exit immediately if a pipeline command fails
set -e

echo "Running deploy pipeline..."
python3 src/console/commands/deploy_pipeline.py

echo "Starting Streamlit application..."
streamlit run app.py
