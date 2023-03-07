from netmiko import ConnectHandler


def switch_save():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.save_config()

def switch_logout():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.disconnect()