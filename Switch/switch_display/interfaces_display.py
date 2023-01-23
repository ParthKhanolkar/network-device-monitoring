from connect import *

#def grab_interfaces():
    
def display_ip_interfaces():
    return ssh_connect.send_command('show ip interface brief')

def display_interface_info():
    return ssh_connect.send_command('show interfaces')

def display_interfaces_description():
    return ssh_connect.send_command('show interfaces description column')

def display_interface_status():
    return ssh_connect.send_command('show interfaces status')