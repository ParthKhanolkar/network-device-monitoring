from connect import *
'''
def grab_interfaces():
    interface_dict = ssh_connect.send_command('show ip interface brief',use_textfsm=True)
    interface_name_list = []
        for i in range(0, len(x)):
        interface_name_list.append(x[i]['intf'])
    return interface_name_list
'''
def display_ip_interfaces():
    return ssh_connect.send_command('show ip interface brief')

def display_interface_info():
    return ssh_connect.send_command('show interfaces')

def display_interfaces_description():
    return ssh_connect.send_command('show interfaces description')

def display_interface_status():
    ssh_connect.enable()
    return ssh_connect.send_command('show interfaces stats')