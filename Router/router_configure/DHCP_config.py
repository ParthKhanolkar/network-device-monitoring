from netmiko import ConnectHandler

#dhcp server
def dhcp_exclude_address(exclude_start_ip,exclude_end_ip):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip dhcp excluded-address ' + exclude_start_ip + ' ' + exclude_end_ip])
    

def dhcp_pool(pool_name,pool_ip,pool_submask,DNS_server,domain_name,default_router):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip dhcp pool ' + pool_name, 'network ' + pool_ip + ' ' + pool_submask, 'dns-server ' + DNS_server, 'domain-name ' + domain_name, 'default-router ' + default_router, 'lease infinite'])


#dhcp relay agent
def dhcp_relay_int(relay_interface,interface_ip):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + relay_interface, 'ip helper-address ' + interface_ip])

#dhcp client
def dhcp_client_int(client_interface):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + client_interface, 'ip address dhcp'])