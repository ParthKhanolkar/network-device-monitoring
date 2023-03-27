from connect import *

#dhcp server
def dhcp_exclude_address(ip,submask):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip dhcp excluded-address ' + ip + ' ' + submask])
    

def dhcp_pool(pool_name,ip,submask,dns_server,domain_name,default_router):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip host ' + pool_name + ' ' + ip, 'network ' + ip + ' ' + submask, 'dns-server ' + dns_server, 'domain-name ' + domain_name, 'default-router ' + default_router, 'lease infinite'])


#dhcp relay agent
def dhcp_relay_int(interface,ip):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + interface, 'ip helper-address ' + ip])

#dhcp client
def dhcp_client_int(interface,ip):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + interface, 'ip address dhcp'])