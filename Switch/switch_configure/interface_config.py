from netmiko import ConnectHandler

def configure_interface_layer_2(int_name,int_speed,int_duplex,int_description):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface '+ int_name , 'no negotiation auto', 'speed ' + int_speed , 'duplex ' + int_duplex , 'description ' + int_description])

def create_loopback_interface(loopb_number):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    #0-2147483647
    ssh_connect.send_config_set(['interface loopback ' + loopb_number])