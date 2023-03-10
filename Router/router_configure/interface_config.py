from netmiko import ConnectHandler

def configure_interface_layer_3(int_name,int_ip,int_sub_mask,int_description):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['interface '+ int_name, 'ip address ' + int_ip + ' ' + int_sub_mask , 'no shutdown' , 'description ' + int_description])

