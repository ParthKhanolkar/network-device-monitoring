from netmiko import ConnectHandler

def add_vlan_subinterfaces(int_name, vlan_number, ip_address, subnet_mask):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + int_name, 'no shutdown', 'interface ' + int_name + '.' + vlan_number, 'encapsulation dot1q ' + vlan_number, 'ip address ' + ip_address + ' ' + subnet_mask])

def router_add_native_vlan(sub_interface, native_vlan):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + sub_interface, 'encapsulation dot1q ' + native_vlan + ' native'])