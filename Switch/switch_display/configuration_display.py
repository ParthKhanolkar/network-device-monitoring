from connect import *
def show_running_configuration():
    ssh_connect.enable()
    return ssh_connect.send_command('show running-config')

def show_startup_configuration():
    ssh_connect.enable()
    return ssh_connect.send_command('show startup-config')


