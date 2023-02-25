from netmiko import ConnectHandler

def display_info_on_hover():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    version_info = ssh_connect.send_command('show version',use_textfsm=True)
    return("Hostname: " + version_info[0]['hostname'] + "\n" + "Version: " + version_info[0]['version'] + "\n" + "Running Image: " + version_info[0]['running_image'])