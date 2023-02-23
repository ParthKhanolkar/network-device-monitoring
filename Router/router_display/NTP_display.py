from netmiko import ConnectHandler
from connect import get_ssh_connect
def display_clock():
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show clock detail')

def display_calendar():
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show calendar')

def display_ntp_status():
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show ntp status')

def display_ntp_associations():
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show ntp associations')