
import hpilo
import json
import requests

ilo = hpilo.Ilo('BRVMH7ESX2-iLO', 'Admin', 'your_password')

# Get General info.
print(ilo.get_fw_version())
print ("Product Name: ", ilo.get_product_name())
print("Serial Number: ", ilo.get_host_data()[1]['Serial Number'])
print("Server Name: ",ilo.get_server_name())
print("Server FQDN: ", ilo.get_server_fqdn())
print("Asset tag: ",ilo.get_asset_tag()['asset_tag'])
print("Uid Status: ",ilo.get_uid_status())
#print(ilo.get_global_settings())
