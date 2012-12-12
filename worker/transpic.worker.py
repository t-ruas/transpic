import urllib
import urllib2
import json
import logging
import xml.dom.minidom

# BPCE specific
urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({"http": "127.0.0.1:8080", "https": "127.0.0.1:8080"})))

# Configure log file
logging.basicConfig(
    filename="transpic.worker.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    )

# Microsoft Translator V2 HTTP API implementation
# http://msdn.microsoft.com/en-us/library/ff512419.aspx
class MsTranslatorApi:
    
    svc_url = "http://api.microsofttranslator.com/V2/Http.svc/"
    auth_url = "https://datamarket.accesscontrol.windows.net/v2/OAuth2-13"

    access_token = None

    def __init__(self):
        pass
        
    def translate(self, text, lang):
        params = {
            "text": text,
            "to": lang,
            "contentType": "text/plain"
            }
        request_url = self.svc_url + "Translate?" + urllib.urlencode(params)
        logging.info("Translation requested [" + text + "] to [" + lang + "]")
        request = urllib2.Request(request_url)
        response_raw = self.execute_authenticated_request(request)
        response_xml = xml.dom.minidom.parseString(response_raw)
        result = response_xml.childNodes[0].firstChild.nodeValue
        logging.info("Translation retrieved [" + result + "]")
        return result
        
    def execute_authenticated_request(self, request):
        self.authenticate_request(request)
        try:
            return urllib2.urlopen(request).read()
        except urllib2.HTTPError as err:
            if err.code == 400:
                logging.info("Access token expired.")
                self.access_token = None
                self.authenticate_request(request)
                return urllib2.urlopen(request).read()
            else:
                raise
    
    def authenticate_request(self, request):
        if self.access_token is None:
            logging.info("Requesting an access token.")
            params = {
                "client_id": "transpic",
                "client_secret": "",
                "scope": "http://api.microsofttranslator.com",
                "grant_type": "client_credentials"
                }
            response_raw = urllib2.urlopen(self.auth_url, urllib.urlencode(params)).read()
            response_json = json.loads(response_raw)
            self.access_token = response_json.get("access_token")
            logging.info("Access token retrieved.")
        request.add_header("Authorization", "Bearer " + self.access_token)

try:
    ms_api = MsTranslatorApi()
    ms_api.translate("bonjour", "en")
    raw_input()
    ms_api.translate("au revoir", "en")
    raw_input()
    ms_api.translate("3ème essai", "en")
except Exception as err:
    logging.error(err)
