#!/bin/bash

# Define the name of the virtual environment
VENV_NAME="audio_venv"

# Create a virtual environment
virtualenv $VENV_NAME

# Activate the virtual environment
source ./$VENV_NAME/bin/activate

# Install necessary Python packages
pip install numpy pyaudio aubio

echo "Setup complete. Virtual environment '$VENV_NAME' is ready."
echo "You can activate it using 'source $VENV_NAME/bin/activate'."

