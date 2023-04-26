from flask import Flask, redirect, url_for, render_template, request, flash, session, current_app
from flask_mail import Mail, Message
from netmiko import ConnectHandler
from netmiko import (NetmikoTimeoutException, NetmikoAuthenticationException)
from paramiko.ssh_exception import SSHException
from router_main import router_main
from switch_main import switch_main


app = Flask(__name__)
app.register_blueprint(router_main)
app.register_blueprint(switch_main)

app.config['MAIL_SERVER']='127.0.0.1'
app.config['MAIL_PORT'] = 1025
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
mail = Mail(app)
app.secret_key = "ywZlyASUtzbr5hZqJy74pSQSck8GPSPb"
with app.app_context():
    current_app.config["ssh_connect"] = None



@app.route('/')
def main():
    return render_template("login.html")

@app.route("/login", methods=['POST'])
def login():
    ipaddress = request.form['ipaddress']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']  #in dev
    hardware = request.form['hardware']

    if(ipaddress and username and password):

        cisco_device = {'device_type':'cisco_ios', 'ip':ipaddress, 'username':username, 'password':password, 'secret':password}
        
        try:
            ssh_connect = ConnectHandler(**cisco_device) 

            current_app.config["ssh_connect"] = ssh_connect
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
            session['user'] = cisco_device.copy()
            session['user']['email'] = email #in dev
            if(hardware == "router"):
                return(redirect('/router'))
            elif(hardware == "switch"):
                return(redirect('/switch'))
            
    else:
        flash("Please fill out all fields")
        return(render_template("login.html"))


def get_ssh_connect():
    return current_app.config["ssh_connect"]






if __name__ == "__main__":
    app.run(debug=True)