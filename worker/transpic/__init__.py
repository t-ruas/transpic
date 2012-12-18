
import ConfigParser
from os import path
import inspect
import urllib2
import flask
import logging

app = flask.Flask(__name__)

# get root directory
script_path = path.dirname(path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)) + "\\"

# read the configuration file
config = ConfigParser.RawConfigParser()
config.read(script_path + "transpic.conf")

# BPCE specific
urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({"http": "127.0.0.1:8080", "https": "127.0.0.1:8080"})))

# Configure log file
logging.basicConfig(
    filename="transpic.worker.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    )

import views

if __name__ == "__main__":
    app.run(debug=True)
