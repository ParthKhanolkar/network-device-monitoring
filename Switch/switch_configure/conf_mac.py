from netmiko import ConnectHandler
def clear_mac_address_table():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_command('clear mac address-table dynamic')

def clear_specific_mac_address(mac_input):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    
    #print('clear mac address-table dynamic address ' + mac_input)
    ssh_connect.enable()
    ssh_connect.send_command('clear mac address-table dynamic address ' + mac_input)

def clear_specific_mac_interface(interface_input):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    
    #actually entee interface values based on dropdown list
    ssh_connect.enable()
    ssh_connect.send_command('clear mac address-table dynamic interface ' + interface_input)