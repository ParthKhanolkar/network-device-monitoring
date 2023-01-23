from connect import *
def display_clock():
    #ssh_connect.enable()
    return ssh_connect.send_command('show clock detail')

def display_calendar():
    #ssh_connect.enable()
    return ssh_connect.send_command('show calendar')

def display_ntp_status():
    return ssh_connect.send_command('show ntp status')

def display_ntp_associations():
    return ssh_connect.send_command('show ntp associations')