from netmiko import ConnectHandler
from connect import get_ssh_connect
def show_dns_hosts():
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show hosts')