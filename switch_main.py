from flask import Flask, Blueprint, redirect, url_for, render_template, request, flash, session, json, jsonify, Response, current_app
from flask_mail import Mail, Message

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
import Switch.switch_display.syslog as syslog

import Switch.switch_configure.conf_mac as conf_mac
import Switch.switch_configure.interface_config as interface_config
import Switch.switch_configure.vlan_config as vlan_config
import Switch.switch_configure.etherchannel_config as etherchannel_config
import Switch.switch_configure.LLDP_config as LLDP_config
import Switch.switch_configure.NTP_config as NTP_config

import Switch.switch_save_logout.switch_save_and_logout as switch_save_and_logout

@switch_main.route("/switch")
def home():
    if('user' in session):
        return render_template("switch_main.html",hoverData=hover_info_display.display_info_on_hover(), deviceInterfaces=interfaces_display.grab_interfaces())
    else:
        return redirect(url_for("main"))

#ARP
@switch_main.route("/switchArpTable")
def disp_ARP_table():
    return render_template("display_field.html",displayFieldVar=arp.display_arp_table())

#Configuartion display
@switch_main.route("/switchRunConf")
def disp_switch_run_conf():
    return render_template("display_field.html",displayFieldVar=configuration_display.show_running_configuration())

@switch_main.route("/switchStartConf")
def disp_switch_start_conf():
    return render_template("display_field.html",displayFieldVar=configuration_display.show_startup_configuration())

#display MAC
@switch_main.route("/switchMacAddressTable")
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


@switch_main.route('/switchDisplaySyslog')
def disp_switch_syslog():
    return render_template("display_field.html",displayFieldVar=syslog.syslog_display())


#Configure------------------------------------------------------------------------------------------

#MAC address Config
@switch_main.route('/clearMacAddressTable', methods=['GET','POST'])
def clear_MAC_address_table():
    if request.method == 'POST':
        conf_mac.clear_mac_address_table()
        return Response(status=204)


@switch_main.route('/clearSpecificMacAddress', methods=['GET','POST'])
def clear_specific_MAC_address():
    if request.method == 'POST':
        mac_input = request.form.get("mac_input")
        conf_mac.clear_specific_mac_address(mac_input)
        return Response(status=204)
    

@switch_main.route('/clearMacInterface', methods=['GET','POST'])
def clear_specific_MAC_interface():
    if request.method == 'POST':
        interface_input = request.form.get("interface_input")
        conf_mac.clear_specific_mac_interface(interface_input)
        return Response(status=204)
    
#Switch interface
@switch_main.route('/switchIntConfigLayerTwo', methods=['GET','POST'])
def switch_interface_config_layer2():
    if request.method == 'POST':
        int_name = request.form.get("int_name")
        int_speed = request.form.get("int_speed")
        int_duplex = request.form.get("int_duplex")
        int_description = request.form.get("int_description")
        interface_config.configure_interface_layer_2(int_name, int_speed, int_duplex, int_description)
        return Response(status=204)

@switch_main.route('/switchAddLoopbackInterface', methods=['GET','POST'])
def switch_conf_loopback_int():
    if request.method == 'POST':
        loopb_number = request.form.get("loopb_number")
        interface_config.create_loopback_interface(loopb_number)
        return Response(status=204)

#VLAN Config
@switch_main.route('/swithCreateVlan', methods=['GET','POST'])
def switch_create_vlan_config():
    if request.method == 'POST':
        vlan_number = request.form.get("vlan_number")
        vlan_name = request.form.get("vlan_name")
        vlan_config.create_vlan(vlan_number,vlan_name)
        return Response(status=204)
    
@switch_main.route('/switchCreateTrunkInterface', methods=['GET','POST'])
def switch_create_vlan_trunk_interface_config():
    if request.method == 'POST':
        bef_int = request.form.get("bef_int")
        vlan_config.create_trunk_interface(bef_int)
        return Response(status=204)

#EtherChannel Config
@switch_main.route('/switchEtherChannelLoadBalanceConfig', methods=['GET','POST'])
def switch_etherchennel_load_balance_config():
    if request.method == 'POST':
        lbtype = request.form.get("lbtype")
        etherchannel_config.etherchannel_loadbalance_config(lbtype)
        return Response(status=204)

@switch_main.route('/switchEtherChannelLacpConfig', methods=['GET','POST'])
def switch_etherchennel_lacp_config():
    if request.method == 'POST':
        interface_range = request.form.get("interface_range")
        channel_group = request.form.get("channel_group")
        LACP_mode = request.form.get("LACP_mode")
        etherchannel_config.etherchannel_LACP_range_config(interface_range,channel_group,LACP_mode)
        return Response(status=204)

#LLDP config
@switch_main.route('/switchLldpGlobalEnable', methods=['GET','POST'])
def switch_lldp_global_enable():
    if request.method == 'POST':
        LLDP_config.LLDP_global_enable()
        return Response(status=204)
    
@switch_main.route('/switchLldpIntEnable', methods=['GET','POST'])
def switch_lldp_int_enable():
    if request.method == 'POST':
        lldp_interface = request.form.get("lldp_interface")
        LLDP_config.LLDP_interface_enable(lldp_interface)
        return Response(status=204)
    
@switch_main.route('/switchLldpTimerConfig', methods=['GET','POST'])
def switch_lldp_timer_config():
    if request.method == 'POST':
        timer_time = request.form.get("timer_time")
        LLDP_config.lldp_timer_config(timer_time)
        return Response(status=204)
    
@switch_main.route('/switchLldpHoldtimeConfig', methods=['GET','POST'])
def switch_lldp_holdtime_config():
    if request.method == 'POST':
        holdtime_time = request.form.get("holdtime_time")
        LLDP_config.lldp_holdtime_config(holdtime_time)
        return Response(status=204)
    
@switch_main.route('/switchLldpReinitConfig', methods=['GET','POST'])
def switch_lldp_reinit_config():
    if request.method == 'POST':
        reinit_time = request.form.get("reinit_time")
        LLDP_config.lldp_reinit_config(reinit_time)
        return Response(status=204)

#switch NTP config
@switch_main.route('/switchSetClockConfig', methods=['GET','POST'])
def switch_ntp_set_clock_config():
    if request.method == 'POST':
        hour = request.form.get("hour")
        minute = request.form.get("minute")
        second = request.form.get("second")
        day = request.form.get("day")
        month = request.form.get("month")
        year = request.form.get("year")
        NTP_config.set_clock(hour,minute,second,day,month,year)
        return Response(status=204)

@switch_main.route('/switchSetCalendarConfig', methods=['GET','POST'])
def switch_ntp_set_calendar_config():
    if request.method == 'POST':
        cal_hour = request.form.get("cal_hour")
        cal_minute = request.form.get("cal_minute")
        cal_second = request.form.get("cal_second")
        cal_day = request.form.get("cal_day")
        cal_month = request.form.get("cal_month")
        cal_year = request.form.get("cal_year")
        NTP_config.set_calendar(cal_hour,cal_minute,cal_second,cal_day,cal_month,cal_year)
        return Response(status=204)
    
@switch_main.route('/switchReadCalendarConfig', methods=['GET','POST'])
def switch_ntp_read_calendar_config():
    if request.method == 'POST':
        NTP_config.sync_clock_to_calendar()
        return Response(status=204)
    
@switch_main.route('/switchUpdateCalendarConfig', methods=['GET','POST'])
def switch_ntp_update_calendar_config():
    if request.method == 'POST':
        NTP_config.sync_calendar_to_clock()
        return Response(status=204)

@switch_main.route('/switchTimezoneConfig', methods=['GET','POST'])
def switch_ntp_timezone_config():
    if request.method == 'POST':
        timezone = request.form.get("timezone")
        hours = request.form.get("hours")
        minutes = request.form.get("minutes")
        NTP_config.set_clock_timezone_offset(timezone,hours,minutes)
        return Response(status=204)
    
@switch_main.route('/switchSummerTimeConfig', methods=['GET','POST'])
def switch_ntp_summertime_config():
    if request.method == 'POST':
        timezone = request.form.get("timezone")
        start_week_number = request.form.get("start_week_number")
        start_day = request.form.get("start_day")
        start_month = request.form.get("start_month")
        start_hour = request.form.get("start_hour")
        start_minute = request.form.get("start_minute")
        end_week_number = request.form.get("end_week_number")
        end_day = request.form.get("end_day")
        end_month = request.form.get("end_month")
        end_hour = request.form.get("end_hour")
        end_minute = request.form.get("end_minute")
        offset = request.form.get("offset")
        NTP_config.clock_summer_time_recurring_config(timezone,start_week_number,start_day,start_month,start_hour,start_minute,end_week_number,end_day,end_month,end_hour,end_minute,offset)
        return Response(status=204)

@switch_main.route('/switchAddNtpServer', methods=['GET','POST'])
def switch_ntp_addserver_config():
    add_server_ntp = request.form.get("add_server_ntp")
    NTP_config.add_ntp_server(add_server_ntp)
    return Response(status=204)

@switch_main.route('/switchNtpSourceLoopbackConfig', methods=['GET','POST'])
def switch_ntp_source_loopback_config():
    loopback_int = request.form.get("loopback_int")
    NTP_config.add_ntp_source_loopback(loopback_int)
    return Response(status=204)

@switch_main.route('/switchNtpMasterConfig', methods=['GET','POST'])
def switch_ntp_master_config():
    NTP_config.ntp_master()
    return Response(status=204)

@switch_main.route('/switchSave')
def save():
    switch_save_and_logout.switch_save()
    return Response(status=204)
        

@switch_main.route('/switchLogout')
def logout():
    #delete session info
    with current_app.app_context():
        mail = Mail()
        msg = Message(subject='configuration data from ' + session['user']['ip'], sender = 'NDMAS@BEproject.com', recipients = [session['user']['email']])
        msg.body = render_template("email.html",Device_data = tech_support.show_os_version_json(), SysLog = syslog.syslog_display())
        mail.send(msg)
        switch_save_and_logout.switch_logout()
        session.pop('user', None)
        return redirect(url_for("main"))
