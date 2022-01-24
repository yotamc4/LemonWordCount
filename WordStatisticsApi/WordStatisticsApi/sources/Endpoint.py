import json
import sys
import flask
from sources import LogicManager
from http import HTTPStatus
from flask import request

app = flask.Flask(__name__)

TYPE = "type"
WORD = "word"
COUNT = "count"
DATA = "data"
JSON_CONTENT_TYPE = "application/json"


@app.route("/word_counter", methods=['POST'])
def word_counter():
    try:
        json_dict = request.get_json()
        data_type, data = json_dict[TYPE], json_dict[DATA]
    except:
        return _build_response(HTTPStatus.BAD_REQUEST, "Invalid request structure")
    if logic_manager.log_data(data, data_type):
        return _build_response(HTTPStatus.ACCEPTED, "Success")
    return _build_response(HTTPStatus.INTERNAL_SERVER_ERROR, "Could not load data to the server")


@app.route("/word_statistics", methods=['GET'])
def word_statistics():
    try:
        parsed_json = request.get_json()
        word = parsed_json[WORD]
    except:
        return _build_response(HTTPStatus.BAD_REQUEST, "Invalid request structure")
    if not word:
        return _build_response(HTTPStatus.BAD_REQUEST, "Invalid input")
    count = logic_manager.get_word_count(word)
    if count is None:
        return _build_response(HTTPStatus.INTERNAL_SERVER_ERROR)
    return _build_query_response(HTTPStatus.OK, {COUNT: count})


def _build_response(status_code, message=""):
    return app.response_class(
        status=status_code,
        mimetype=JSON_CONTENT_TYPE,
        response=json.dumps(message)
    )


def _build_query_response(status_code, body):
    return app.response_class(
        status=status_code,
        mimetype=JSON_CONTENT_TYPE,
        response=json.dumps(body)
    )


if __name__ == "__main__":
    logic_manager = LogicManager.LogicManager()
    if len(sys.argv) > 2:
        port = int(sys.argv[1])
        host = sys.argv[2]
    else:
        host = "localhost"
        port = 5000
    app.run(host=host, port=port)
