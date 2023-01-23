from connect import *
def display_mac_address_table():
    return ssh_connect.send_command('show mac address-table')

