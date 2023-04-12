from netmiko import ConnectHandler

def create_vlan(vlan_number,vlan_name):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['vlan ' + vlan_number, 'name ' + vlan_name])

def create_trunk_interface(bef_int):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + bef_int, 'switchport trunk encapsulation dot1q', 'switchport mode trunk'])
    #add for allowed vlan, native vlan
    #return("Trunk interface created")
