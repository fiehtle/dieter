#! /bin/bash

# Colors for terminal output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🚀 Setting up Dieter development environment..."

# check if virtal environment exists
if [ ! -d "venv" ]; then
    echo "${YELLOW}Creating virtual environment...${NC}"
    python -m venv venv
fi

# Activate virtual environment
echo "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Install/upgrade pip
python -m pip install --upgrade pip

# Install dependencies
echo "${YELLOW}Installing dependencies...${NC}"
pip install -r requirements.txt

echo "${GREEN}✨ Setup complete! Virtual environment activated and dependencies installed.${NC}"
echo "${GREEN}🎹 Ready to build some synth modules!${NC}"







