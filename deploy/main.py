from azure import *
from azure.servicemanagement import *
import ConfigParser
import os
import inspect
import urllib2

# get configuration directory
conf_path = os.path.dirname(os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)) + "\\..\\..\\transpic.deploy\\"

# read the configuration file
config = ConfigParser.RawConfigParser()
config.read(conf_path + "deploy.conf")

# get service management credentials
waz_subscription_id = config.get("azure", "subscription_id")
waz_certificat_path = conf_path + config.get("azure", "certificat_file")

# get proxy settings
proxy_host = config.get("proxy", "host")
proxy_port = config.get("proxy", "port")

print(proxy_host)

'''
sms = ServiceManagementService(waz_subscription_id, waz_certificat_path)
sms.set_proxy(proxy_host, proxy_host)

# list hosted services
result = sms.list_hosted_services()
for hosted_service in result:
    print('Service name: ' + hosted_service.service_name)
    print('Management URL: ' + hosted_service.url)
    print('Affinity group: ' + hosted_service.hosted_service_properties.affinity_group)
    print('Location: ' + hosted_service.hosted_service_properties.location)
    print('')
'''
