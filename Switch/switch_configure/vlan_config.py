from connect import *

def create_vlan():
    ssh_connect.enable()
    vlan_number = input("Enter the number of the VLAN you want to create: ")
    vlan_name = input("Enter name of the VLAN: ")
    ssh_connect.send_config_set(['vlan ' + vlan_number, 'name ' + vlan_name])
    return("VLAN is created!")

def create_trunk_interface():
    ssh_connect.enable()
    bef_int = input("Enter the interface you want to be a trunk: ")
    ssh_connect.send_config_set(['interface ' + bef_int, 'switchport trunk encapsulation dot1q', 'switchport mode trunk'])
    #add for allowed vlan, native vlan
    return("Trunk interface created")
