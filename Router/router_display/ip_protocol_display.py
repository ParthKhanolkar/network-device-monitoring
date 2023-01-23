from connect import *
def show_ip_protocols():
    #ssh_connect.enable()
    return ssh_connect.send_command('show ip protocols')