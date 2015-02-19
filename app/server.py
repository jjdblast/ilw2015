__author__ = 'theopavlakou'

from flask import jsonify, request, url_for
import json

from app import app
import datetime

@app.route("/get_coords", methods=["GET", 'POST'])
def get_map_coords():
    #TODO Now we will fake the results
    # print(type(request.form["offset"]))
    # print(request.form["offset"])
    print("Initial Date is: ")
    print(request.form['initial_date'])
    date_list = request.form["initial_date"].split('/')
    # print(date_list)
    print("Actual date is: ")
    d = datetime.datetime.strptime(request.form["initial_date"], "%d/%m/%y")
    print(d)

    points = []
    if (int(request.form["offset"])==0):
        points.append({"location":(55.951663, -3.206273), "weight": 10})
        points.append({"location":(55.950000, -3.206273), "weight": 10})
    elif (int(request.form["offset"])==10):
        points.append({"location":(55.950000, -3.160000), "weight": 10})
        points.append({"location":(55.945555, -3.162111), "weight": 10})
    j_points = json.dumps({"points":points})
    return j_points


