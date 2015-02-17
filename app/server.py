__author__ = 'theopavlakou'

from flask import jsonify, request

from app import app

@app.route("/get_coords", methods=['POST'])
def get_map_coords():
    return str(request.form)
    # return jsonify({'message': request.data})
    return jsonify({'message': request.data})