from netmiko import ConnectHandler

def display_lldp_info():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show lldp')

def display_lldp_traffic():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show lldp traffic')

def display_lldp_interface():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show lldp interface')

def display_lldp_neighbours():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show lldp neighbors')

def display_lldp_neighbours_detail():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show lldp neighbors detail')