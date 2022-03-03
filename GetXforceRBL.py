# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
import json
import sys

# Get ip input in sys argument, query in RBL xforce and return score.
# User for Zabbix monitoring item to evaluate if ip is in blacklist or poor reputation. 


# IP that will be queried by parameter / argument delivered to the script in the console.
ip_RBL = sys.argv

# Concatenation of api + IP address queried.
url = ("https://api.xforce-example.ibmcloud.com/ipr/{}".format(ip_RBL[1]))

# Gets data in JSON format of IP queried.
ipr_api_xforce = requests.get(url, auth=HTTPBasicAuth('api key here', 'api key here'))

# Converts variable content ipr_api_xforce (Json) to dictionary.
ipr_api_xforcejson = json.loads(ipr_api_xforce.content)

# Access the ['score'] key and print the IP reputation score passed as argument in the 'ip_RBL' variable.
print(float(ipr_api_xforcejson['score']))
