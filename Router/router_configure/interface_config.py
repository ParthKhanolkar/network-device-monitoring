from connect import *

def configure_interface_layer_3():
    int_name = input("Enter the interface you want to configure: ")
    int_ip = input("Enter th ip address you want to assign: ")
    int_sub_mask = input("Enter the subnet mask: ")
    int_description = input("Enter the description of the interface: ")
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface '+ int_name, 'ip address ' + int_ip + ' ' + int_sub_mask , 'no shutdown' , 'description ' + int_description])

