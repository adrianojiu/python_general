import hpilo
import json
import requests

ilo_servers = ['BRSRV4DBO1-ILO','BRSRV4DBO2-ILO']

for s_ilo in ilo_servers:
    ilo = hpilo.Ilo(s_ilo, 'Admin', 'your_password')

    #Get SNMP settings.
    l = "------------------------"
    ls = "########################"
    print(ls)
    print(s_ilo)
    print(l)
    print(ilo.get_product_name())
    print("Numero de serie: ", ilo.get_host_data()[1]['Serial Number'])
    print(l)
    print("SNMP habilitado: ", ilo.get_snmp_im_settings()["snmp_access"])
    print("Porta SNMP: ", ilo.get_snmp_im_settings()["snmp_port"])
    print("Comunidade RO SNMP 1: ", ilo.get_snmp_im_settings()["snmp_address_1_rocommunity"])
    l2 = l * 2
    print (l2)
