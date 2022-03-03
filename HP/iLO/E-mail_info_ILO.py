
import hpilo
import json
import requests

# Get e-mail settings.

ilo_servers = ['TEST-SRV4DBO1-ILO','TEST-SRV4DBO2-ILO','TEST-VMH7ESX01-iLO','TEST-VMH7ESX02-iLO']

for s_ilo in ilo_servers:
    ilo = hpilo.Ilo(s_ilo, 'Admin', 'YourPassword')

    l = "------------------------"
    ls = "########################"
    print(ls)
    print(ilo.get_server_name())
    print(l)
    print(ilo.get_product_name())
    print("Numero de serie: ", ilo.get_host_data()[1]['Serial Number'])
    print(l)
    print("Email de Altertas: ", ilo.get_global_settings()["alertmail_email_address"])
    print("Alerta de email ativo: ", ilo.get_global_settings()["alertmail_enable"])
    print("Email alterta remetente: ", ilo.get_global_settings()["alertmail_sender_domain"])
    print("Email alterta porta smtp: ", ilo.get_global_settings()["alertmail_smtp_port"])
    print("Email alterta servidor SMTP: ", ilo.get_global_settings()["alertmail_smtp_server"])
    l2 = l * 2
    print (l2)
