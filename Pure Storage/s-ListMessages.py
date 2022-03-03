import purestorage
import urllib3
urllib3.disable_warnings() # Disables warnin certificate for Pure array
import json

# Pure storage rest client doc
# https://pure-storage-python-rest-client.readthedocs.io/en/stable/quick_start.html#before-you-begin


# List events in Pure Storage Array

array = purestorage.FlashArray( "10.70.10.10", api_token="type_your_API_token_here", verify_https=False )
messages_array = array.list_messages()

msg_more_recent1 = messages_array[-1]['current_severity'],messages_array[-1]['event'],messages_array[-1]['code'],messages_array[-1]['id']
msg_more_recent2 = messages_array[-2]['current_severity'],messages_array[-2]['event'],messages_array[-2]['code'],messages_array[-2]['id']
msg_more_recent3 = messages_array[-3]['current_severity'],messages_array[-3]['event'],messages_array[-3]['code'],messages_array[-3]['id']
msg_more_recent4 = messages_array[-4]['current_severity'],messages_array[-4]['event'],messages_array[-4]['code'],messages_array[-4]['id']


print (msg_more_recent1[0])
print (msg_more_recent1[1])

if "warning" in msg_more_recent1[0] and "warning" in msg_more_recent1[1]:
    print("warning")

array.invalidate_cookie()
