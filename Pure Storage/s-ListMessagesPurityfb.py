# Pure storage rest client doc
# https://pure-storage-python-rest-client.readthedocs.io/en/stable/quick_start.html#before-you-begin


from purity_fb import PurityFb, rest
import urllib3
urllib3.disable_warnings()

fb = PurityFb("10.70.10.10") # assume the array IP is 10.255.9.28
#fb.disable_verify_ssl()
try:
    res = fb.login("type_your_API_token_here") # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        res = fb.alerts.list_alerts()
        print(res)
        # list alerts and sort by severity
        res = fb.alerts.list_alerts(sort='severity')
    except rest.ApiException as e:
        print("Exception when listing alert: %s\n" % e)
