from netmiko import ConnectHandler

def enable_portfast(interface):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + interface, 'spanning-tree portfast'])

def enable_bpdu_guard(interface):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + interface, 'spanning-tree bpduguard enable'])

def enable_bpdu_guard_all():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['spanning-tree portfast bpduguard default'])

def pvst_mode(mode):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['spanning-tree mode ' + mode])

def spanning_tree_vlan_priority(vlan_number,priority):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['spanning-tree vlan ' + vlan_number + 'priority ' + priority])

def spanning_tree_vlan_root(vlan_number,root_priority):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['spanning-tree vlan ' + vlan_number + 'root ' + root_priority])

def spanning_tree_vlan_cost(vlan_number,cost):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['spanning-tree vlan ' + vlan_number + 'cost ' + cost])

def spanning_tree_vlan_port_priority(vlan_number,port_priority):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['spanning-tree vlan ' + vlan_number + 'port-priority ' + port_priority])

def rstp_link_type(link_type):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['spanning-tree link-type ' + link_type])

