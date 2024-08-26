#!/usr/bin/env python -B
# Instructions for running and debugging this python file in VSCode
# The program assumes that you have python3 and pip3 installed on your machine.
# In the VSCode terminal window type the following:
#    pip3 install -r requirements.txt

import sys 
sys.dont_write_bytecode = True
from app import app
from flask_cors import CORS

if __name__ == "__main__":
    CORS(app)
    app.run(debug=True)
