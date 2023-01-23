from connect import *
def syslog_display():
    ssh_connect.enable()
    return(ssh_connect.send_command('show logging'))
    #ssh_connect.disconnect()