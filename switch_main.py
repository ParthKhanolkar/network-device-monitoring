from flask import Flask, Blueprint, redirect, url_for, render_template, request, flash, session, json, jsonify, Response

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
import Switch.switch_display.hover_info_display as hover_info_display

import Switch.switch_configure.conf_mac as conf_mac
import Switch.switch_configure.interface_config as interface_config
import Switch.switch_configure.vlan_config as vlan_config
import Switch.switch_configure.etherchannel_config as etherchannel_config
import Switch.switch_configure.LLDP_config as LLDP_config
import Switch.switch_configure.NTP_config as NTP_config


@switch_main.route("/switch")
def home():
    if('user' in session):
        return render_template("switch_main.html",hoverData=hover_info_display.display_info_on_hover())
    else:
        return redirect(url_for("main"))

#ARP
@switch_main.route("/switchArpTable")
def disp_ARP_table():
    return render_template("display_field.html",displayFieldVar=arp.display_arp_table())

#Configuartion display
@switch_main.route("/switchRunConf")
def disp_switch_run_conf():
    #if request.method == 'POST':
    #datavar = jsonify(request.form)
    #print(datavar)
    #html_item = json.dumps(request.form, indent=2, separators=(', ', ': '))
    #print(html_item)
    #return('',204)
    return render_template("display_field.html",displayFieldVar=configuration_display.show_running_configuration())

@switch_main.route("/switchStartConf")
def disp_switch_start_conf():
    return render_template("display_field.html",displayFieldVar=configuration_display.show_startup_configuration())

#display MAC
@switch_main.route("/switchStartConf")
def disp_MAC_table():
    return render_template("display_field.html",displayFieldVar=dis_mac.display_mac_address_table())

#interfaces display
@switch_main.route("/switchIpIntBr")
def disp_IP_int():
    return render_template("display_field.html",displayFieldVar=interfaces_display.display_ip_interfaces())

@switch_main.route("/switchIpIntInfo")
def disp_IP_info():
    return render_template("display_field.html",displayFieldVar=interfaces_display.display_interface_info())

@switch_main.route("/switchIpIntDesc")
def disp_IP_int_desc():
    return render_template("display_field.html",displayFieldVar=interfaces_display.display_interfaces_description())

@switch_main.route("/switchIpIntStats")
def disp_IP_int_stats():
    return render_template("display_field.html",displayFieldVar=interfaces_display.display_interface_status())

#tech support
@switch_main.route("/switchDisplayBuffers")
def disp_router_buffers():
    return render_template("display_field.html",displayFieldVar=tech_support.display_buffers())

@switch_main.route("/switchDisplayStacks")
def disp_router_stacks():
    return render_template("display_field.html",displayFieldVar=tech_support.display_stacks())

@switch_main.route("/switchDisplayMemoryPros")
def disp_router_memory_process():
    return render_template("display_field.html",displayFieldVar=tech_support.display_processes_memory())

@switch_main.route("/switchDisplayCpuPros")
def disp_router_cpu_process():
    return render_template("display_field.html",displayFieldVar=tech_support.display_processes_cpu())

@switch_main.route("/switchDisplayFileSys")
def disp_router_file_systems():
    return render_template("display_field.html",displayFieldVar=tech_support.display_file_systems())

@switch_main.route("/switchDisplayOsVer")
def disp_router_os_versiom():
    return render_template("display_field.html",displayFieldVar=tech_support.show_os_version())
 
@switch_main.route("/switchDisplayFlashMemory")
def disp_router_flash_memory(): 
    return render_template("display_field.html",displayFieldVar=tech_support.show_flash_memory())

#vlan display
@switch_main.route("/switchDisplayVlanInterfaces")
def disp_switch_vlan_int():
    return render_template("display_field.html",displayFieldVar=vlan_display.display_vlans_interfaces())

@switch_main.route("/switchDisplayVlanTrunkInterfaces")
def disp_switch_trunk_int():
    return render_template("display_field.html",displayFieldVar=vlan_display.display_trunk_interfaces())

#etherchannel display
@switch_main.route("/switchDisplayEtherchannelLoadbalance")
def disp_switch_eth_ch_loadb():
    return render_template("display_field.html",displayFieldVar=etherchannel_display.etherchannel_loadbalance_display())
@switch_main.route("/switchDisplayEtherchannelSummary")
def disp_switch_eth_ch_summary():
    return render_template("display_field.html",displayFieldVar=etherchannel_display.etherchannel_summary_display())
@switch_main.route("/switchDisplayEtherchannelPortchannel")
def disp_switch_eth_ch_portch():
    return render_template("display_field.html",displayFieldVar=etherchannel_display.etherchannel_portchannel_display())

#LLDP display
@switch_main.route("/switchLldpInfo")
def disp_LLDP_info():
    return render_template("display_field.html",displayFieldVar=LLDP_display.display_lldp_info())

@switch_main.route("/switchLldpTraffic")
def disp_LLDP_traffic():
    return render_template("display_field.html",displayFieldVar=LLDP_display.display_lldp_traffic())

@switch_main.route("/switchLldpInterface")
def disp_LLDP_interface():
    return render_template("display_field.html",displayFieldVar=LLDP_display.display_lldp_interface())

@switch_main.route("/switchLldpNeighbours")
def disp_LLDP_neighbours():
    return render_template("display_field.html",displayFieldVar=LLDP_display.display_lldp_neighbours())

@switch_main.route("/switchLldpNeighboursDetail")
def disp_LLDP_neighbours_detail():
    return render_template("display_field.html",displayFieldVar=LLDP_display.display_lldp_neighbours_detail())

#NTP display
@switch_main.route("/switchNtpClockDetail")
def disp_SW_NTP_clock_detail():
    return render_template("display_field.html",displayFieldVar=NTP_display.display_clock())

@switch_main.route("/switchNtpCalendar")
def disp_SW_NTP_calendar():
    return render_template("display_field.html",displayFieldVar=NTP_display.display_calendar())

@switch_main.route("/switchNtpStatus")
def disp_SW_NTP_status():
    return render_template("display_field.html",displayFieldVar=NTP_display.display_ntp_status())

@switch_main.route("/switchNtpAssociations")
def disp_SW_NTP_associations():
    return render_template("display_field.html",displayFieldVar=NTP_display.display_ntp_associations())