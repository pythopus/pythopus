#!/bin/bash

# PYTHOPUS API
# Script to run the flask application in development mode.

export FLASK_APP=app.py
export FLASK_ENV=development
pip install -r requirements.txt
flask run
