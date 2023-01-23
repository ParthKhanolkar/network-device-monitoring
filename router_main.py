from connect import *

import Router.router_display.tech_support as tech_support
import Router.router_display.interfaces_display as interfaces_display
import Router.router_display.syslog as syslog
import Router.router_display.configuration_display as configuration_display

import Router.router_configure.ip_routes as ip_routes
import Router.router_configure.interface_config as interface_config

print(cisco_device['device_type'])