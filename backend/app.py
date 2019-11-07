from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)


# return all shows in the database, with optional parameter for minEpisodes
@app.route("/shows", methods=["GET"])
def get_all_shows():
    minEpisodes = request.args.get("minEpisodes")
    shows = db.get("shows")
    if minEpisodes is not None:
        if int(minEpisodes) < 0:
            return create_response(
                message="minEpisodes must be zero or more", status=400
            )
        result = []
        for show in shows:
            if show["episodes_seen"] >= int(minEpisodes):
                result.append(show)
        return create_response({"shows": result})
    return create_response({"shows": shows})


# get show by ID
@app.route("/shows/<id>", methods=["GET"])
def get_show(id):
    if db.getById("shows", int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    show = db.getById("shows", int(id))
    return create_response(data=show)


# create a new show
@app.route("/shows", methods=["POST"])
def create_show():
    data = request.get_json()
    if data["name"] is None or data["episodes_seen"] is None:
        return create_response(
            status=422, message="One or more required parameters are missing"
        )
    new_show = {"name": data["name"], "episodes_seen": data["episodes_seen"]}
    db.create("shows", new_show)
    return create_response(
        data=new_show, status=201, message="Show created successfully"
    )


# update an existing show
@app.route("/shows/<id>", methods=["PUT"])
def update_show(id):
    if db.getById("shows", int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    data = request.get_json()
    updated_show = db.updateById("shows", int(id), data)
    return create_response(
        data=updated_show, status=201, message="Show updated successfully"
    )


# delete show by ID
@app.route("/shows/<id>", methods=["DELETE"])
def delete_show(id):
    if db.getById("shows", int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById("shows", int(id))
    return create_response(message="Show deleted")


"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
