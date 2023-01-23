from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
from connect import *

def display_vlans_interfaces():
    return ssh_connect.send_command('show vlan brief')

def display_trunk_interfaces():
    return ssh_connect.send_command('show interfaces trunk')