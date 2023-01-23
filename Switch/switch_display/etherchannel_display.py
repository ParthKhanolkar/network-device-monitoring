from connect import *

def etherchannel_loadbalance_display():
    ssh_connect.send_command('show etherchannel load-balance')

def etherchannel_summary_display():
    ssh_connect.send_command('show etherchannel summary')

def etherchannel_portchannel_display():
    ssh_connect.send_command('show etherchannel port-channel')