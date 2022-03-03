from purity_fb import PurityFb, VersionResponse, rest

# Get Pure API version

fb = PurityFb("10.70.100.10") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    # no need to login to get API versions
    res = fb.api_version.list_versions()
    assert isinstance(res, VersionResponse)
    print (res.versions)  # ex: ["1.0", "1.1", "1.2"]
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
    