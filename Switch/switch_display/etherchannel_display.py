from netmiko import ConnectHandler

def etherchannel_loadbalance_display():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.send_command('show etherchannel load-balance')

def etherchannel_summary_display():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.send_command('show etherchannel summary')

def etherchannel_portchannel_display():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.send_command('show etherchannel port-channel')