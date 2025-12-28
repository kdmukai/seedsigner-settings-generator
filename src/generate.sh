#!/bin/bash

# pull the latest from our target SeedSigner fork/branch
git submodule update --remote

# Extract SeedSigner's `SettingsDefinition` and generate the static index.html
python3 extract_settings.py

mv index.html ../docs/.
