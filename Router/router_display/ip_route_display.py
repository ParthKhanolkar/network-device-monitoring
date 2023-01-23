from connect import *
def show_ip_routes():
    #ssh_connect.enable()
    return ssh_connect.send_command('show ip route')
