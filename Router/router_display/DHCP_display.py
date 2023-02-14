from connect import *

#dhcp server
def dhcp_binding_display():
    return ssh_connect.send_command('show ip dhcp binding')