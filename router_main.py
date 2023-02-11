from flask import Flask, Blueprint, redirect, url_for, render_template, request, flash, session, json, jsonify

router_main = Blueprint("router_main", __name__, static_folder="static", template_folder="templates")

import Router.router_display.tech_support as tech_support
import Router.router_display.interfaces_display as interfaces_display
import Router.router_display.syslog as syslog
import Router.router_display.configuration_display as configuration_display
import Router.router_display.ip_protocol_display as ip_protocol_display
import Router.router_display.ip_route_display as ip_route_display
import Router.router_display.LLDP_display as LLDP_display
import Router.router_display.NTP_display as NTP_display

import Router.router_configure.ip_routes as ip_routes
import Router.router_configure.interface_config as interface_config
import Router.router_configure.LLDP_config as LLDP_config
import Router.router_configure.NTP_config as NTP_config
import Router.router_configure.security_configuration as security_configuration


@router_main.route("/router")
def home():
    if('user' in session):
        return render_template("router_main.html")
    else:
        return redirect(url_for("main"))

@router_main.route("/routerrunconf", methods=['POST'])
def disp_run_conf():
    if request.method == 'POST':
        #datavar = jsonify(request.form)
        #print(datavar)
        html_item = json.dumps(request.form, indent=2, separators=(', ', ': '))
        print(html_item)
        #return('',204)
        return render_template("router_main.html",displayvar="html_item")
        

@router_main.route("/routerstartconf")
def disp_start_conf():
    return render_template("router_main.html",displayvar="This is startup configuration")

@router_main.route("/ipintbr")
def disp_IP_int():
    return render_template("router_main.html",displayvar="This is IP Interface")

@router_main.route("/ipintinfo")
def disp_IP_info():
    return render_template("router_main.html",displayvar="This is IP Interface Information")

@router_main.route("/ipintdesc")
def disp_IP_int_desc():
    return render_template("router_main.html",displayvar="This is IP Interface Description")

@router_main.route("/ipintstats")
def disp_IP_int_stats():
    return render_template("router_main.html",displayvar="This is IP Interface Stats")



        
'''
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    #delete session info
    ssh_connect.disconnect()
    session.pop('user', None)
    return flask.redirect(url_for("main"))
    '''
