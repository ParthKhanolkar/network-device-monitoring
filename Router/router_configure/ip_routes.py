from netmiko import ConnectHandler
def add_static_route(dest_ip,subnet_mask,next_hop):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip route ' + dest_ip + ' ' + subnet_mask + ' ' + next_hop])
    #return('Static Route Added!')


def add_rip_route(auto_summary,network_add):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    auto_summary = input("Should automatic network summarization be enabled? (yes or no): ")
    if (auto_summary == "yes"):
        atsmm = ""
    elif (auto_summary == "no"):
        atsmm = "no auto-summary"
    ssh_connect.send_config_set(['router rip', 'version 2', atsmm, 'network ' + network_add])
    #return('RIP Route Added!')
    #Choose passive interfaces as well

def add_eigrp_route(as_number,auto_summary,network_add,wildcard_mask):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    if (auto_summary == "yes"):
        atsmm = ""
    elif (auto_summary == "no"):
        atsmm = "no auto-summary"
    ssh_connect.send_config_set(['router eigrp ' + as_number,  atsmm, 'network ' + network_add + ' ' + wildcard_mask])
    #return('RIP Route Added!')

def add_ospf_route(process_id,network_add,wildcard_mask,ospf_area):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['router ospf ' + process_id, 'network ' + network_add + ' ' + wildcard_mask + ' ' + 'area ' + ospf_area])
    #return('OSPF Route Added!')

def ospf_on_interface(ospf_int,process_id,ospf_area):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + ospf_int, 'ip ospf ' + process_id + ' ' + 'area ' + ospf_area])
    #return('OSPF Route Added!')
    



#add_static_route()

#ssh_connect.disconnect()