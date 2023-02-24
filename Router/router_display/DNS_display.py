from netmiko import ConnectHandler

def show_dns_hosts():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show hosts')