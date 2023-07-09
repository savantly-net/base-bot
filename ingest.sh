# Bash script to ingest data
# Error if any command fails
set -e

python3 base_bot/ingest.py
