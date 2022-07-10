#!/bin/bash
# TODO: Check for python existance
# Set environment
python3 -m venv env
source env/bin/activate
echo "Virtual environment is ready"

# TODO: Check for pip existance
# Install dependecies
pip3 install -r requirements.txt
echo "All dependecies are installed"
