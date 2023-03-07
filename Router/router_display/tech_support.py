from netmiko import ConnectHandler

def display_buffers():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show buffers')

#To monitor the stack usage of processes and interrupt routines
def display_stacks():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show stacks')
 
#To show memory used
def display_processes_memory():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show processes memory')

#displays detailed CPU utilization statistics about the active processes
def display_processes_cpu():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show processes cpu')

def display_file_systems():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    return ssh_connect.send_command('show file systems')

def show_os_version():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show version')

def show_flash_memory():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    return ssh_connect.send_config_set('show flash')