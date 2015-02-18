__author__ = 'theopavlakou'

from flask import jsonify, request

from app import app

@app.route("/get_coords", methods=['POST'])
def get_map_coords():
    return str(request.form)
    # return jsonify({'message': request.data})
    #TODO here we must get the Tweets relevant, turn them
    #into JSON format.
    return jsonify({'message': request.data})