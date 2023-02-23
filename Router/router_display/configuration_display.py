from netmiko import ConnectHandler
from connect import get_ssh_connect
def show_running_configuration():
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    return ssh_connect.send_command('show running-config')

def show_startup_configuration():
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    return ssh_connect.send_command('show startup-config')


