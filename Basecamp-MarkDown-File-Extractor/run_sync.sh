#!/bin/zsh

# Basecamp Sync Script
# Runs both BC2 and BC3 extractors, only fetching new/missing data

SCRIPT_DIR="/Users/mirakozoglu/Documents/Antigravity/Basecamp-MarkDown-File-Extractor"
LOG_FILE="$SCRIPT_DIR/sync.log"
VENV="$SCRIPT_DIR/.venv/bin/activate"

echo "========================================" >> "$LOG_FILE"
echo "Sync started at $(date)" >> "$LOG_FILE"

# Activate virtual environment
source "$VENV"

# Run Basecamp 2 extractor
echo "--- Running Basecamp 2 extractor ---" >> "$LOG_FILE"
cd "$SCRIPT_DIR"
python3 extractor.py >> "$LOG_FILE" 2>&1

# Run Basecamp 3 extractor
echo "--- Running Basecamp 3 extractor ---" >> "$LOG_FILE"
python3 extractor_bc3.py >> "$LOG_FILE" 2>&1

echo "Sync finished at $(date)" >> "$LOG_FILE"
echo "========================================" >> "$LOG_FILE"
