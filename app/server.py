__author__ = 'theopavlakou'

from flask import jsonify, request

from app import app

@app.route("/get_coords", methods=['POST'])
def get_map_coords():

    return jsonify(request.view_args)