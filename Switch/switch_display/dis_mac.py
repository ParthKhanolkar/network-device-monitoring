from netmiko import ConnectHandler
def display_mac_address_table():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show mac address-table')

