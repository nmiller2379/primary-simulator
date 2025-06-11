#!/bin/bash

# Assumes you're already inside the caldwell-campaign-sim directory
# and that README.md and planning.md already exist

# Requirements file (only if you need it)
touch requirements.txt

# Simulator package
mkdir -p simulator
touch simulator/__init__.py
touch simulator/candidate.py
touch simulator/district.py
touch simulator/state.py
touch simulator/events.py
touch simulator/engine.py

# Data directory (no __init__.py needed)
mkdir -p data
touch data/example_districts.json
touch data/voter_blocks.yaml

# Scripts directory
mkdir -p scripts
touch scripts/run_sim.py

# Tests package
mkdir -p tests
touch tests/__init__.py
touch tests/test_candidate.py
touch tests/test_district.py
touch tests/test_allocation.py

echo "✅ Project structure created successfully (without overwriting README or planning docs)."
