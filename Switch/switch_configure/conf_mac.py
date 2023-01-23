from connect import *
def clear_mac_address_table():
    #ssh_connect.enable()
    ssh_connect.send_command('clear mac address-table dynamic')

def clear_specific_mac_address():
    mac_input = input("Enter the mac address you want to be removed: ")
    #print('clear mac address-table dynamic address ' + mac_input)
    #ssh_connect.enable()
    print('clear mac address-table dynamic address ' + mac_input)
    ssh_connect.send_command('clear mac address-table dynamic address ' + mac_input)

def clear_specific_mac_interface():
    interface_input = input("Enter the interface: ")
    #actually entee interface values based on dropdown list
    #ssh_connect.enable()
    print('clear mac address-table dynamic interface ' + interface_input)
    ssh_connect.send_command('clear mac address-table dynamic interface ' + interface_input)