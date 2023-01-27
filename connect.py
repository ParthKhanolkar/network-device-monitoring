from flask import Flask, redirect, url_for, render_template, request
from netmiko import ConnectHandler
from netmiko import (NetmikoTimeoutException, NetmikoAuthenticationException)
from paramiko.ssh_exception import SSHException

app = Flask(__name__)


#create device template
cisco_device = {
'device_type': 'cisco_ios',
'ip': '10.0.0.1',
'username': 'cisco',
'password':'cisco',
'secret':'cisco'
}

@app.route('/')
def main():
    return render_template("login.html")

@app.route("/login", methods=['POST'])
def login():
    ipaddress = request.form['ipaddress']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    hardware = request.form['hardware']

    return(render_template("router_main.html", username=username, ip=ipaddress, email=email))
	   



'''
try:
    ssh_connect = ConnectHandler(**cisco_device)
except NetmikoTimeoutException:
    print("Device not reachable")
except NetmikoAuthenticationException:
    print("Authentication Failure")
except SSHException:
    print("Make sure SSH is enabled")

'''

if __name__ == "__main__":
    app.run(debug=True)