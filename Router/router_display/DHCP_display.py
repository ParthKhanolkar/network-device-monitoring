from netmiko import ConnectHandler


#dhcp server
def dhcp_binding_display():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show ip dhcp binding')