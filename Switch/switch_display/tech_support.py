from connect import *
def display_buffers():
    return ssh_connect.send_command('show buffers')

#To monitor the stack usage of processes and interrupt routines
def display_stacks():
    return ssh_connect.send_command('show stacks')

#To show memory used
def display_processes_memory():
    return ssh_connect.send_command('show show processes memory')

#displays detailed CPU utilization statistics about the active processes
def display_buffers():
    return ssh_connect.send_command('show processes cpu')


def display_file_systems():
    return ssh_connect.send_command('show file systems')

def show_os_version():
    return ssh_connect.send_command('show version')

def show_flash_memory():
    return ssh_connect.send_command('show flash')