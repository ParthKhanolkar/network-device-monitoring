from netmiko import ConnectHandler

def create_vlan(vlan_number,vlan_name):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['vlan ' + vlan_number, 'name ' + vlan_name])

def configure_vlan_interfaces(vlan_number, int_range):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface range ' + int_range, 'switchport mode access', 'switchport access vlan ' + vlan_number])

def create_trunk_interface(bef_int):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + bef_int, 'switchport trunk encapsulation dot1q', 'switchport mode trunk'])

def trunk_allowed_vlan(trunk_int, allowed_vlan):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + trunk_int,'switchport trunk allowed vlan ' + allowed_vlan])

def trunk_allowed_vlan(trunk_int, native_vlan):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + trunk_int,'switchport trunk native vlan ' + native_vlan])