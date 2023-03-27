from netmiko import ConnectHandler

def config_router_ip_dns():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip dns server'])
    

def dns_add_ip_host(dns_hostname, dns_ip):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip host ' + dns_hostname + ' ' + dns_ip])

def ip_name_server(dns_server_ip):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip name-server ' + dns_server_ip])

def perform_dns_queries():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip domain lookup'])

def set_domain_name(domain_name):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.sned_config_set(['ip domain name ' + domain_name])