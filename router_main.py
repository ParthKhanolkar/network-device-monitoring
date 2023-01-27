from connect import *

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

'''
@app.route("/")
def home():
    return render_template("router_main.html", device=cisco_device)'''
