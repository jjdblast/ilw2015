__author__ = 'theopavlakou'

from flask import jsonify, request, url_for
import json

from app import app

@app.route("/get_coords", methods=["GET", 'POST'])
def get_map_coords():
    #TODO Now we will fake the results
    print(type(request.form["data_value"]))
    print(request.form["data_value"])
    points = []
    if (int(request.form["data_value"])==0):
        points.append({"location":(55.951663, -3.206273), "weight": 10})
        points.append({"location":(55.950000, -3.206273), "weight": 10})
    elif (int(request.form["data_value"])==10):
        points.append({"location":(55.950000, -3.160000), "weight": 10})
        points.append({"location":(55.945555, -3.162111), "weight": 10})
    j_points = json.dumps({"points":points})
    print(j_points)
    print({"points": points})
    return j_points


