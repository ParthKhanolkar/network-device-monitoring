from connect import *
def display_arp_table():
    return ssh_connect.send_command('show arp')
