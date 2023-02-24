from netmiko import ConnectHandler
def display_clock():
    #ssh_connect.enable()
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show clock detail')

def display_calendar():
    #ssh_connect.enable()
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show calendar')

def display_ntp_status():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show ntp status')

def display_ntp_associations():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show ntp associations')