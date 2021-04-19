#!/bin/bash

# Before running this script, install miniconda or anaconda with Python 3.7
# https://conda.io/docs/user-guide/install/macos.html

# After installing either miniconda or anaconda, open a new terminal code so conda is on the path
# Must cd into this directory to run this script successfully

# Setup the environment for the classroom. TeachOps FTW!
set -e # Exit immediately if a command exits with a non-zero status
set -x # Exit immediately if a pipeline exits with a non-zero status

# Environment name is from environment.yml
envname=$(sed '1!d' environment.yml | sed 's/^.* //')

# Create environment 
conda update --name base conda -y 
conda env create --name $envname --force 

# Start environment
conda activate $envname
# Note: You might get at "CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'."
# Then manually run start the env and manually run the remaining commands


# Update during development
# conda update --all --yes 
# # Pin right before teaching
# conda env export > environment environment.yml

# Enable extensions
jupyter contrib nbextension install --sys-prefix
jupyter nbextension enable spellchecker/main
jupyter nbextension enable codefolding/main
jupyter nbextension install rise --py --sys-prefix
jupyter nbextension enable rise --py --sys-prefix

# Note: This shell script comes with no warranty or support. It is just an aid to help you create a reproducible enirovnment for the course. Your computer might not play nice with it, and this script depends on The Internet which changes.