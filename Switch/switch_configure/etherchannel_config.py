from netmiko import ConnectHandler

def etherchannel_loadbalance_config(lbtype):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set[('port-channel load-balance ' + lbtype)]

def etherchannel_LACP_range_config(interface_range,channel_group,LACP_mode):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface range ' + interface_range, 'channel-group ' + str(channel_group) + ' mode ' + LACP_mode])
    ssh_connect.send_config_set(['interface port-channel ' + str(channel_group), 'switchport mode trunk'])