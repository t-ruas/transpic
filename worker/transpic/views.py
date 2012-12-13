
import uuid
import ConfigParser
import os
import inspect
import flask
import time
import urllib2

from transpic.worker import app
from transpic.worker import translation
from transpic.worker import ocr

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

# BPCE specific
urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({"http": "127.0.0.1:8080", "https": "127.0.0.1:8080"})))

# Configure log file
logging.basicConfig(
    filename="transpic.worker.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    )

# receive posted pictures
@app.route('/add', methods=['POST'])
def add():
        pass

# try:
    # ms_api = MsTranslatorApi()
    # ms_api.translate("bonjour", "en")
    # raw_input()
    # ms_api.translate("au revoir", "en")
    # raw_input()
    # ms_api.translate("3ème essai", "en")
# except Exception as err:
    # logging.error(err)
