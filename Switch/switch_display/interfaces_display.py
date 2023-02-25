from netmiko import ConnectHandler
#from connect import get_ssh_connect

#def grab_interfaces():
    
def display_ip_interfaces():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show ip interface brief')

def display_interface_info():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show interfaces')

def display_interfaces_description():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show interfaces description')

def display_interface_status():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show interfaces status')