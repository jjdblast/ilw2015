__author__ = 'theopavlakou'

from flask import jsonify, request, url_for
import json

from app import app
import datetime
from parse import parse

@app.route("/get_coords", methods=["GET", 'POST'])
def get_map_coords():
    initial_date = datetime.datetime.strptime(request.form["initial_date"], "%d/%m/%y")
    new_date = datetime.timedelta(days=int(request.form['offset'])) + initial_date
    print("Initial date is: ")
    initial_date_string = initial_date.strftime("%d-%m-%y")
    print(initial_date_string)
    print("New date is: ")
    new_date_string = new_date.strftime("%d-%m-%y")
    print(new_date_string)
    file_string = new_date_string+".txt"
    # new_date_string = "19-02-20159.txt"

    dict_to_jsonify = parse(file_string)

    j_points = json.dumps(dict_to_jsonify)
    return j_points


