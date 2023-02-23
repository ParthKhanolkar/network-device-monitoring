from netmiko import ConnectHandler
from connect import get_ssh_connect
def display_lldp_info():
    ssh_connect = get_ssh_connect()
    ssh_connect.send_command('show lldp')

def display_lldp_traffic():
    ssh_connect = get_ssh_connect()
    ssh_connect.send_command('show lldp traffic')

def display_lldp_interface():
    ssh_connect = get_ssh_connect()
    ssh_connect.send_command('show lldp interface')

def display_lldp_neighbours():
    ssh_connect = get_ssh_connect()
    ssh_connect.send_command('show lldp neighbours')

def display_lldp_neighbours_detail():
    ssh_connect = get_ssh_connect()
    ssh_connect.send_command('show lldp neighbours detail')