__author__ = 'theopavlakou'

from flask import jsonify, request, url_for

from app import app

@app.route("/get_coords", methods=["GET", 'POST'])
def get_map_coords():
    #TODO Now we will fake the results
    print(request.form["data_value"])
    print(jsonify({"message": request.form["data_value"]}))
    return jsonify(message=request.form["data_value"])


