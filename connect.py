from netmiko import ConnectHandler
from netmiko import (NetmikoTimeoutException, NetmikoAuthenticationException)
from paramiko.ssh_exception import SSHException
#create device template
cisco_device = {
'device_type': 'cisco_ios',
'ip': '10.0.0.1',
'username': 'cisco',
'password':'cisco',
'secret':'cisco'
}

try:
    ssh_connect = ConnectHandler(**cisco_device)
except NetmikoTimeoutException:
    print("Device not reachable")
except NetmikoAuthenticationException:
    print("Authentication Failure")
except SSHException:
    print("Make sure SSH is enabled")




#ssh_connect.disconnect()


