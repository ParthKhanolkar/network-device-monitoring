from netmiko import ConnectHandler

def update_from_flash(source,destination, remote_host, source_filename, destination_filename):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['copy ' + source + ': ' + destination + ': ', remote_host, source_filename, destination_filename])
    ssh_connect.send_config_set(['boot system ' + destination_filename])
    ssh_connect.save_config()