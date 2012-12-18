
import flask
import logging
import translation
from transpic import app

class StatusValues:
    new = 1
    received = 2
    converted = 3
    recognized = 4
    translated = 5

class RunningProcess:
    status = StatusValues.new
    text = ""

# receive posted pictures
@app.route("/do_image", methods=["POST"])
def do_image():
    pass

# receive posted pictures
@app.route("/do_text", methods=["GET"])
def do_text():
    ms_api = translation.MsTranslatorApi()
    return ms_api.translate(flask.request.files.get("text"), "fr")
