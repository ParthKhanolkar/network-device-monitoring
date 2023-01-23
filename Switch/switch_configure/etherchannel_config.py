from connect import *

def etherchannel_loadbalance_config():
    ssh_connect.enable()
    lbtype = input("Enter the load balancing configuration: ")
    ssh_connect.send_config_set[('port-channel load-balance ' + lbtype)]

def etherchannel_LACP_range_config():
    ssh_connect.enable()
    interface_range = input("Enter interface range: ")
    LACP_mode = input("Enter LACP mode: ")
    ssh_connect.send_config_set(['interface range ' + interface_range, 'channel-group 1 mode ' + LACP_mode])
    ssh_connect.send_config_set(['interface port-channel 1', 'switchport mode trunk'])