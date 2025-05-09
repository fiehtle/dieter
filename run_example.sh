#!/bin/bash

# Colors for terminal output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "${YELLOW}Running Dieter Synth Example: $1${NC}"

# Ensure Python can find our modules
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Run the example
python python/examples/$1.py

echo "${GREEN}Example completed!${NC}" 