
from netmiko import ConnectHandler
from connect import get_ssh_connect

def router_save():
    ssh_connect = get_ssh_connect()
    ssh_connect.save_config()

def router_logout():
    ssh_connect = get_ssh_connect()
    ssh_connect.disconnect()
    