from connect import *

def configure_interface_layer_2():
    int_name = input("Enter the interface you want to configure: ")
    int_speed = input("Enter the speed of the interface (mbps): ")
    int_duplex = input("Enter the duplex mode: ")
    int_description = input("Enter the description of the interface: ")
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface '+ int_name , 'no negotiation auto', 'speed ' + int_speed , 'duplex ' + int_duplex , 'description ' + int_description])