from flask import Flask, Blueprint, redirect, url_for, render_template, request, flash, session

switch_main = Blueprint("switch_main", __name__, static_folder="static", template_folder="templates")

import Switch.switch_display.arp as arp
import Switch.switch_display.configuration_display as configuration_display
import Switch.switch_display.dis_mac as dis_mac
import Switch.switch_display.interfaces_display as interfaces_display
import Switch.switch_display.tech_support as tech_support
import Switch.switch_display.vlan_display as vlan_display
import Switch.switch_display.etherchannel_display as etherchannel_display
import Switch.switch_display.LLDP_display as LLDP_display
import Switch.switch_display.NTP_display as NTP_display

import Switch.switch_configure.conf_mac as conf_mac
import Switch.switch_configure.interface_config as interface_config
import Switch.switch_configure.vlan_config as vlan_config
import Switch.switch_configure.etherchannel_config as etherchannel_config
import Switch.switch_configure.LLDP_config as LLDP_config
import Switch.switch_configure.NTP_config as NTP_config


@switch_main.route("/switch")
def home():
    if('user' in session):
        return render_template("switch_main.html", username=session['user']['username'], ip=session['user']['ip'])
    else:
        return redirect(url_for("main"))