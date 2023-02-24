from netmiko import ConnectHandler

def show_ip_routes():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    return ssh_connect.send_command('show ip route')
