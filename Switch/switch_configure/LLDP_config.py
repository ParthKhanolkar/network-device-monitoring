from netmiko import ConnectHandler

def LLDP_global_enable():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['lldp run'])

def LLDP_interface_enable(lldp_interface):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface ' + lldp_interface, 'lldp transmit', 'lldp receive'])

def lldp_timer_config(timer_time):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['lldp timer ' + timer_time])

def lldp_holdtime_config(holdtime_time):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['lldp holdtime ' + holdtime_time])

def lldp_reinit_config(reinit_time):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['lldp reinit ' + reinit_time])