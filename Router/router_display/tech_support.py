from netmiko import ConnectHandler
from connect import get_ssh_connect
def display_buffers():
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show buffers')

#To monitor the stack usage of processes and interrupt routines
def display_stacks():
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show stacks')
 
#To show memory used
def display_processes_memory():
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show processes memory')

#displays detailed CPU utilization statistics about the active processes
def display_processes_cpu():
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show processes cpu')

def display_file_systems():
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    return ssh_connect.send_command('show file systems')

def show_os_version():
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show version')

def show_flash_memory():
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    return ssh_connect.send_command('show flash')