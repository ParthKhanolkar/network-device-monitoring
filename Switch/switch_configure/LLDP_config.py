from connect import *

def LLDP_global_enable():
    ssh_connect.enable()
    ssh_connect.send_config_set(['lldp run'])

def LLDP_interface_enable():
    ssh_connect.enable()
    lldp_interface = input("Enter the interface you wnt to enable LLDP on: ")
    ssh_connect.send_config_set(['interface ' + lldp_interface, 'lldp transmit', 'lldp receive'])

def lldp_timer_config():
    ssh_connect.enable()
    timer_time = input("Enter LLDP timer in seconds: ")
    ssh_connect.send_config_set(['lldp timer ' + timer_time])

def lldp_holdtime_config():
    ssh_connect.enable()
    holdtime_time = input("Enter LLDP holdtime in seconds: ")
    ssh_connect.send_config_set(['lldp holdtime ' + holdtime_time])

def lldp_reinit_config():
    ssh_connect.enable()
    reinit_time = input("Enter LLDP timer in seconds: ")
    ssh_connect.send_config_set(['lldp reinit ' + reinit_time])