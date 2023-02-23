from netmiko import ConnectHandler
from connect import get_ssh_connect
def syslog_display():
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    return(ssh_connect.send_command('show logging'))
    #ssh_connect.disconnect()