from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
from netmiko import ConnectHandler

def display_vlans_interfaces():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show vlan brief')

def display_trunk_interfaces():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show interfaces trunk')