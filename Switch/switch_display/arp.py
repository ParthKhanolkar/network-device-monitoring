from netmiko import ConnectHandler
def display_arp_table():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show arp')
