from flask import Flask, redirect, url_for, render_template, request, flash, session
from netmiko import ConnectHandler
from netmiko import (NetmikoTimeoutException, NetmikoAuthenticationException)
from paramiko.ssh_exception import SSHException

app = Flask(__name__)
app.secret_key = "secret key"

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

    cisco_device = {'device_type':'cisco_ios', 'ip':ipaddress, 'username':username, 'password':password}
    #session['login'] = cisco_device
    try:
        ssh_connect = ConnectHandler(**cisco_device)    
    except NetmikoTimeoutException:
        flash("Device not reachable")
        return(render_template("login.html"))
    except NetmikoAuthenticationException:
        flash("Authentication Failure")
        return(render_template("login.html"))
    except SSHException:
        flash("Make sure SSH is enabled")
        return(render_template("login.html"))
    else:
        if(hardware == "router"):
            return(render_template("router_main.html", username=username, ip=ipaddress, email=email))
        elif(hardware == "switch"):
            return(render_template("switch.html", username=username, ip=ipaddress, email=email))



    
	   








if __name__ == "__main__":
    app.run(debug=True)