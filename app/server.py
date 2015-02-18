__author__ = 'theopavlakou'

from flask import jsonify, request, url_for

from app import app

@app.route("/get_coords", methods=["GET", 'POST'])
def get_map_coords():
    #TODO Now we will fake the results
    print(request.form["data_value"])
    points = []
    points.append({"location":(55.951663, -3.206273), "weight": 10})
    points.append({"location":(52.951663, -1.206273), "weight": 10})
    points.append({"location":(51.951663, -2.206273), "weight": 10})
    print({"points": points})
    return jsonify({"points": points})


