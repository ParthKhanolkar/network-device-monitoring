from netmiko import ConnectHandler
#from connect import get_ssh_connect
def grab_interfaces():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    interface_dict = ssh_connect.send_command('show ip interface brief',use_textfsm=True)
    interface_name_list = []
    for i in range(0, len(interface_dict)):
        interface_name_list.append(interface_dict[i]['intf'])
    return interface_name_list

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
    #ssh_connect.enable()
    return ssh_connect.send_command('show interfaces stats')