from connect import *

def config_router_ip_dns():
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip dns server'])
    

def dns_add_ip_host(hostname, ip):
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip host ' + hostname + ' ' + ip])

def ip_name_server(ip):
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip name-server ' + ip])

def perform_dns_queries():
    ssh_connect.enable()
    ssh_connect.send_config_set(['ip domain lookup'])

def set_domain_name(domain_name):
    ssh_connect.enable()
    ssh_connect.sned_config_set(['ip domain name ' + domain_name])