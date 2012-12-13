
import uuid
import ConfigParser
import os
import inspect
import flask
import time
import urllib2

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

# get root directory
script_path = os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)) + "\\"

# read the configuration file
config = ConfigParser.RawConfigParser()
config.read(script_path + "transpic.conf")

process_status = {}

# main page
@app.route("/", methods=["GET", "POST"])
def main():
    if flask.request.method == "GET":
        # initial request, show a file upload form
        return flask.render_template('upload.html')
    else:
        # after upload, show a progress bar
        # generate an uuid to rename the image and act as an id for status handling
        id = uuid.uuid5(uuid.NAMESPACE_DNS, "transpic.com")
        # save the image
        image = flask.request.files.get("image_name")
        #image.save(config.get("upload", "path") + str(id))
        process_status[id] = RunningProcess()
        return flask.render_template("progress.html", id=id)

# status handling service
@app.route('/status', methods=['GET', 'POST'])
def status():
    if flask.request.method == "GET":
        # ajax status request from the progress page
        id = flask.request.args.get("id")
        if id not in process_status:
            return "{'result':0}";
        while process_status[id].status != StatusValues.translated:
            # todo: timeout
            time.sleep(1)
        # todo: cleanup dictionary after a while
        return "{'result':1,'text':'" + process_status[id].text + "'}";
    else:
        # status update called from the different components
        pass
