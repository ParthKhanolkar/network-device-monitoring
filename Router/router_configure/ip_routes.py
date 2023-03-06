from netmiko import ConnectHandler
def add_static_route(dest_ip,subnet_mask,next_hop):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    #dest_ip = input("Enter the destination ipv4 address: ")
    #subnet_mask = input("Enter the subnet mask of the destination ipv4 address: ")
    #next_hop = input("Enter the next-hop ipv4 address: ")
    ssh_connect.send_config_set(['ip route ' + dest_ip + ' ' + subnet_mask + ' ' + next_hop])
    #return('Static Route Added!')


def add_rip_route():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    auto_summary = input("Should automatic network summarization be enabled? (yes or no): ")
    if (auto_summary == "yes"):
        atsmm = ""
    elif (auto_summary == "no"):
        atsmm = "no auto-summary"
    network_add = input("Enter the network address of interface on which RIP will activate: ")
    ssh_connect.send_config_set(['router rip', 'version 2', atsmm, 'network ' + network_add])
    return('RIP Route Added!')
    #Choose passive interfaces as well

def add_eigrp_route():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    as_number = input("Enter the EIGRP Autonomous system number: ")
    auto_summary = input("Should automatic network summarization be enabled? (yes or no): ")
    if (auto_summary == "yes"):
        atsmm = ""
    elif (auto_summary == "no"):
        atsmm = "no auto-summary"
    network_add = input("Enter the network address of interface on which EIGRP will activate: ")
    wildcard_mask = input("Enter the wildcard mask of the interface on which EIGRP will activate: ")
    ssh_connect.send_config_set(['router eigrp ' + as_number,  atsmm, 'network ' + network_add + ' ' + wildcard_mask])
    return('RIP Route Added!')

def add_ospf_route():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    process_id = input("Enter the OSPF process ID: ")
    network_add = input("Enter the network address of interface on which EIGRP will activate: ")
    wildcard_mask = input("Enter the wildcard mask of the interface on which EIGRP will activate: ")
    ospf_area = input("Enter the OSPF area: ")
    ssh_connect.send_config_set(['router ospf ' + process_id, 'network ' + network_add + ' ' + wildcard_mask + ' ' + 'area ' + ospf_area])
    return('OSPF Route Added!')

def ospf_on_interface():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ospf_int = input("Enter the interface you want OSPF to be activated on: ")
    process_id = input("Enter the OSPF process ID: ")
    ospf_area = input("Enter the OSPF area: ")
    ssh_connect.send_config_set(['interface ' + ospf_int, 'ip ospf ' + process_id + ' ' + 'area ' + ospf_area])
    return('OSPF Route Added!')
    



#add_static_route()

#ssh_connect.disconnect()