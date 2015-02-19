#!flask/bin/python

from app import app
import os
app.run(debug=True)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FILES = os.path.join(APP_ROOT, 'data')
app.config['DATA_FILES'] = DATA_FILES
