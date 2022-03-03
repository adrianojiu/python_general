import socket
from requests.auth import HTTPBasicAuth
import requests
import json
import datetime
import timestring
from datetime import timedelta

# Get information about warranty hardware Dell.

apiKey = 'type your api key here'
serviceTag = 'type servive tag here'

#Connect to Dell TechDirect API, insert api key and service tag using String parameter after the signal "%"
apiEndpointConnect = requests.get('https://api.dellexample.com/support/assetinfo/v4/getassetwarranty/%s?apikey=%s' % (serviceTag,apiKey))

#Convert above content to Json
apiEndpointConnect_json = json.loads(apiEndpointConnect.content)

#Get device model
getModelo = apiEndpointConnect_json["AssetWarrantyResponse"][0]["AssetHeaderData"]["MachineDescription"]

#Get warranty end date#
GetWarrantyEndDateKeys = apiEndpointConnect_json["AssetWarrantyResponse"][0]["AssetEntitlementData"][0]["EndDate"][0:10]

#Convert string guarantee end date to date
date_string = GetWarrantyEndDateKeys
date_object = timestring.Date(date_string)

#Current date + 60 days
now = datetime.datetime.now() + timedelta(days=60)

#If the warranty end date is less than 60 days, respond with an end date.
if date_object > now:
    print(GetWarrantyEndDateKeys,",",serviceTag,",",getModelo)
