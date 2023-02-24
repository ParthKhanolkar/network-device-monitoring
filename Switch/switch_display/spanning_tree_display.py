from netmiko import ConnectHandler

def show_spanning_tree():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.send_command('show spanning tree')