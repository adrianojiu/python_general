

import hpilo
import json
import requests

ilo_servers = ['BRSRV4DBO1-ILO','BRSRV4DBO2-ILO','BRVMH7ESX01-iLO','BRVMH7ESX02-iLO']

for s_ilo in ilo_servers:
    ilo = hpilo.Ilo(s_ilo, 'Admin', 'your_password')

    # Get hardware Health Status
    # Full return
    #print(ilo.get_embedded_health())

    l = "------------------------"
    ls = "########################"
    print(ls)
    print(ilo.get_server_name())
    print(l)
    print(ilo.get_product_name())
    print("Numero de serie: ", ilo.get_host_data()[1]['Serial Number'])
    print(l)
    print("Health Status Bios" ,ilo.get_embedded_health()["health_at_a_glance"]["bios_hardware"]["status"])
    print("Health Status Fans" ,ilo.get_embedded_health()["health_at_a_glance"]["fans"]["status"])
    print("Health Status Memory" ,ilo.get_embedded_health()["health_at_a_glance"]["memory"]["status"])
    print("Health Status Network" ,ilo.get_embedded_health()["health_at_a_glance"]["network"]["status"])
    print("Health Status CPU" ,ilo.get_embedded_health()["health_at_a_glance"]["processor"]["status"])
    print("Health Status Storage" ,ilo.get_embedded_health()["health_at_a_glance"]["storage"]["status"])
    print("Health Status Temperature" ,ilo.get_embedded_health()["health_at_a_glance"]["temperature"]["status"])
    l2 = l * 2
    print (l2)
