
import hpilo
import json
import requests

ilo_servers = ['BRSRV4DBO1-ILO','BRSRV4DBO2-ILO','BRVMH7ESX01-iLO','BRVMH7ESX02-iLO']

for s_ilo in ilo_servers:
    ilo = hpilo.Ilo(s_ilo, 'Admin', 'your_password')
    
    # Get ip and DNS settings.
    l = "------------------------"
    ls = "########################"
    print(ls)
    print(ilo.get_server_name())
    print(l)
    print(ilo.get_product_name())
    print("Numero de serie: ", ilo.get_host_data()[1]['Serial Number'])
    print(l)
    print("IP ", ilo.get_network_settings()["ip_address"])
    print("Mac ", ilo.get_network_settings()["mac_address"])
    print("DNS Primario ", ilo.get_network_settings()["sec_dns_server"])
    print("DNS Primario ", ilo.get_network_settings()["sec_dns_server"])
    print("DNS Secundario ", ilo.get_network_settings()["prim_dns_server"])
    print("DNS Terciario ", ilo.get_network_settings()["ter_dns_server"])
    l2 = l * 2
    print (l2)
