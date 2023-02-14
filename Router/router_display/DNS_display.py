from connect import *

def show_dns_hosts():
    return ssh_connect.send_command('show hosts')