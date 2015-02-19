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
    new_date_string = "19-02-2015.txt"

    d = parse(new_date_string)
    points = []
    if (int(request.form["offset"])==0):
        points.append({"location":(55.951663, -3.206273), "weight": 10})
        points.append({"location":(55.950000, -3.206273), "weight": 10})
    elif (int(request.form["offset"])==10):
        points.append({"location":(55.950000, -3.160000), "weight": 10})
        points.append({"location":(55.945555, -3.162111), "weight": 10})
    j_points = json.dumps({"points":points})
    return j_points


