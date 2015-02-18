__author__ = 'theopavlakou'

from flask import jsonify, request, url_for
import json

from app import app

@app.route("/get_coords", methods=["GET", 'POST'])
def get_map_coords():
    #TODO Now we will fake the results
    print(request.form["data_value"])
    points = []
    points.append({"location":(55.951663, -3.206273), "weight": 10})
    points.append({"location":(55.954708, -3.302416), "weight": 12})
    points.append({"location":(55.97194, -3.224334), "weight": 2})
    points.append({"location":(55.959472, -3.249847), "weight": 4})
    j_points = json.dumps({"points":points})
    print(j_points)
    print({"points": points})
    return j_points


