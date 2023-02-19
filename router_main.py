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

@router_main.route("/routerRunConf")
def disp_router_run_conf():
    #if request.method == 'POST':
    #datavar = jsonify(request.form)
    #print(datavar)
    #html_item = json.dumps(request.form, indent=2, separators=(', ', ': '))
    #print(html_item)
    #return('',204)
    return render_template("router_main.html",displayvar="html_item")
        

@router_main.route("/routerStartConf")
def disp_router_start_conf():
    return render_template("router_main.html",displayvar="This is startup configuration")

@router_main.route("/routerIpIntBr")
def disp_IP_int():
    return render_template("router_main.html",displayvar="This is IP Interface")

@router_main.route("/routerIpIntInfo")
def disp_IP_info():
    return render_template("router_main.html",displayvar="This is IP Interface Information")

@router_main.route("/routerIpIntDesc")
def disp_IP_int_desc():
    return render_template("router_main.html",displayvar="This is IP Interface Description")

@router_main.route("/routerIpIntStats")
def disp_IP_int_stats():
    return render_template("router_main.html",displayvar="This is IP Interface Stats")

@router_main.route("/routerIpProto")
def disp_IP_protocols():
    return render_template("router_main.html",displayvar="This is IP Protocols")

@router_main.route("/routerIpRoute")
def disp_IP_routes():
    return render_template("router_main.html",displayvar="This is IP Routes")

@router_main.route("/routerLldpInfo")
def disp_LLDP_info():
    return render_template("router_main.html",displayvar="This is LLDP info")

@router_main.route("/routerLldpTraffic")
def disp_LLDP_traffic():
    return render_template("router_main.html",displayvar="This is LLDP Traffic")

@router_main.route("/routerLldpInterface")
def disp_LLDP_interface():
    return render_template("router_main.html",displayvar="This is LLDP Interface")

@router_main.route("/routerLldpNeighbours")
def disp_LLDP_neighbours():
    return render_template("router_main.html",displayvar="This is LLDP Neighbours")

@router_main.route("/routerLldpNeighboursDetail")
def disp_LLDP_neighbours_detail():
    return render_template("router_main.html",displayvar="This is LLDP Neighbours Detail")

@router_main.route("/routerNtpClockDetail")
def disp_IP_NTP_clock_detail():
    return render_template("router_main.html",displayvar="This is NTP Clock Detail")

@router_main.route("/routerNtpCalendar")
def disp_IP_NTP_calendar():
    return render_template("router_main.html",displayvar="This is NTP Calendar")

@router_main.route("/routerNtpStatus")
def disp_IP_NTP_status():
    return render_template("router_main.html",displayvar="This is NTP Status")

@router_main.route("/routerNtpAssociations")
def disp_IP_NTP_associations():
    return render_template("router_main.html",displayvar="This is NTP Associations")
'''
@router_main.route("/routerDisplayBuffers")
def disp_IP_LLDP_info():
    return render_template("router_main.html",displayvar="This is Buffers")

@router_main.route("/routerDisplayStacks")
def disp_IP_LLDP_info():
    return render_template("router_main.html",displayvar="This is Stacks")

@router_main.route("/routerDisplayMemoryPros")
def disp_IP_LLDP_info():
    return render_template("router_main.html",displayvar="This is Memory Processes")

@router_main.route("/routerDisplayCpuPro")
def disp_IP_LLDP_info():
    return render_template("router_main.html",displayvar="This is CPU Processes")

@router_main.route("/routerDisplaySyslog")
def disp_IP_LLDP_info():
    return render_template("router_main.html",displayvar="This is Router Syslog")
'''



        
'''
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    #delete session info
    ssh_connect.disconnect()
    session.pop('user', None)
    return flask.redirect(url_for("main"))
    '''
