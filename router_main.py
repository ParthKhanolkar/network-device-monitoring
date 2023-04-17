from flask import Flask, Blueprint, redirect, url_for, render_template, request, flash, session, json, jsonify, Response, current_app
from flask_mail import Mail, Message

router_main = Blueprint("router_main", __name__, static_folder="static", template_folder="templates")



import Router.router_display.tech_support as tech_support
import Router.router_display.interfaces_display as interfaces_display
import Router.router_display.syslog as syslog
import Router.router_display.configuration_display as configuration_display
import Router.router_display.ip_protocol_display as ip_protocol_display
import Router.router_display.ip_route_display as ip_route_display
import Router.router_display.LLDP_display as LLDP_display
import Router.router_display.NTP_display as NTP_display
import Router.router_display.DHCP_display as DHCP_display
import Router.router_display.DNS_display as DNS_display
import Router.router_display.hover_info_display as hover_info_display

import Router.router_configure.ip_routes as ip_routes
import Router.router_configure.interface_config as interface_config
import Router.router_configure.LLDP_config as LLDP_config
import Router.router_configure.NTP_config as NTP_config
import Router.router_configure.security_configuration as security_configuration
import Router.router_configure.DNS_config as DNS_config
import Router.router_configure.DHCP_config as DHCP_config
import Router.router_configure.update_os as update_os
import Router.router_configure.vlan_config as vlan_config

import Router.router_save_logout.router_save_and_logout as router_save_and_logout





@router_main.route("/router")
def home():
    if('user' in session):
        return render_template("router_main.html",hoverData=hover_info_display.display_info_on_hover(), deviceInterfaces=interfaces_display.grab_interfaces())
    else:
        return redirect(url_for("main"))
'''
def send_email_after_logout():
    msg = Message('Hello from the other side!', sender =   'alexandra@mailtrap.io', recipients = [session['user']['email']])
    msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
    mail.send(msg)
    return "Message sent!"
'''


#Display------------------------------------------------------------------------------------------
#configuration_display
@router_main.route("/routerRunConf")
def disp_router_run_conf():
    return render_template("display_field.html",displayFieldVar=configuration_display.show_running_configuration())
        

@router_main.route("/routerStartConf")
def disp_router_start_conf():
    return render_template("display_field.html",displayFieldVar=configuration_display.show_startup_configuration())

#interfaces_display
@router_main.route("/routerIpIntBr")
def disp_IP_int():
    return render_template("display_field.html",displayFieldVar=interfaces_display.display_ip_interfaces())

@router_main.route("/routerIpIntInfo")
def disp_IP_info():
    return render_template("display_field.html",displayFieldVar=interfaces_display.display_interface_info())

@router_main.route("/routerIpIntDesc")
def disp_IP_int_desc():
    return render_template("display_field.html",displayFieldVar=interfaces_display.display_interfaces_description())

@router_main.route("/routerIpIntStats")
def disp_IP_int_stats():
    return render_template("display_field.html",displayFieldVar=interfaces_display.display_interface_status())

@router_main.route("/routerIpProto")
def disp_IP_protocols():
    return render_template("display_field.html",displayFieldVar=ip_protocol_display.show_ip_protocols())

#ip_route_display
@router_main.route("/routerIpRoute")
def disp_IP_routes():
    return render_template("display_field.html",displayFieldVar=ip_route_display.show_ip_routes())


#LLDP_display
@router_main.route("/routerLldpInfo")
def disp_LLDP_info():
    return render_template("display_field.html",displayFieldVar=LLDP_display.display_lldp_info())

@router_main.route("/routerLldpTraffic")
def disp_LLDP_traffic():
    return render_template("display_field.html",displayFieldVar=LLDP_display.display_lldp_traffic())

@router_main.route("/routerLldpInterface")
def disp_LLDP_interface():
    return render_template("display_field.html",displayFieldVar=LLDP_display.display_lldp_interface())

@router_main.route("/routerLldpNeighbours")
def disp_LLDP_neighbours():
    return render_template("display_field.html",displayFieldVar=LLDP_display.display_lldp_neighbours())

@router_main.route("/routerLldpNeighboursDetail")
def disp_LLDP_neighbours_detail():
    return render_template("display_field.html",displayFieldVar=LLDP_display.display_lldp_neighbours_detail())

#NTP display

@router_main.route("/routerNtpClockDetail")
def disp_IP_NTP_clock_detail():
    return render_template("display_field.html",displayFieldVar=NTP_display.display_clock())

@router_main.route("/routerNtpCalendar")
def disp_IP_NTP_calendar():
    return render_template("display_field.html",displayFieldVar=NTP_display.display_calendar())

@router_main.route("/routerNtpStatus")
def disp_IP_NTP_status():
    return render_template("display_field.html",displayFieldVar=NTP_display.display_ntp_status())

@router_main.route("/routerNtpAssociations")
def disp_IP_NTP_associations():
    return render_template("display_field.html",displayFieldVar=NTP_display.display_ntp_associations())


#Tech support
@router_main.route("/routerDisplayBuffers")
def disp_router_buffers():
    return render_template("display_field.html",displayFieldVar=tech_support.display_buffers())

@router_main.route("/routerDisplayStacks")
def disp_router_stacks():
    return render_template("display_field.html",displayFieldVar=tech_support.display_stacks())

@router_main.route("/routerDisplayMemoryPros")
def disp_router_memory_process():
    return render_template("display_field.html",displayFieldVar=tech_support.display_processes_memory())

@router_main.route("/routerDisplayCpuPros")
def disp_router_cpu_process():
    return render_template("display_field.html",displayFieldVar=tech_support.display_processes_cpu())

@router_main.route("/routerDisplayFileSys")
def disp_router_file_systems():
    return render_template("display_field.html",displayFieldVar=tech_support.display_file_systems())

@router_main.route("/routerDisplayOsVer")
def disp_router_os_versiom():
    return render_template("display_field.html",displayFieldVar=tech_support.show_os_version())
 
@router_main.route("/routerDisplayFlashMemory")
def disp_router_flash_memory(): 
    return render_template("display_field.html",displayFieldVar=tech_support.show_flash_memory())

#syslog
@router_main.route("/routerDisplaySyslog")
def disp_router_syslog():
    return render_template("display_field.html",displayFieldVar=syslog.syslog_display())

#DNS display
@router_main.route("/routerDisplayDnsHosts")
def disp_router_dns_hosts():
    return render_template("display_field.html",displayFieldVar=DNS_display.show_dns_hosts())

#DHCP display
@router_main.route("/routerDisplayIpDhcpBinding")
def disp_router_ip_dhcp_binding():
    return render_template("display_field.html",displayFieldVar=DHCP_display.dhcp_binding_display())


#Configure------------------------------------------------------------------------------------------

#IP routes
@router_main.route('/routerStaticRouteConf', methods=['GET','POST'])
def conf_router_static_route():
    if request.method == 'POST':
        dest_ip = request.form.get("dest_ip")
        subnet_mask = request.form.get("subnet_mask")
        next_hop = request.form.get("next_hop")
        #print('ip route ' + dest_ip + ' ' + subnet_mask + ' ' + next_hop)
        ip_routes.add_static_route(dest_ip,subnet_mask,next_hop)
        return Response(status=204)

@router_main.route('/routerRipRouteConf', methods=['GET','POST'])
def conf_router_rip_route():
    if request.method == 'POST':
        auto_summary = request.form.get("auto_summary")
        network_add = request.form.get("network_add")
        ip_routes.add_rip_route(auto_summary,network_add)
        return Response(status=204)
    
@router_main.route('/routerEigrpRouteConf', methods=['GET','POST'])
def conf_router_eigrp_route():
    if request.method == 'POST':
        as_number = request.form.get("as_number")
        auto_summary = request.form.get("auto_summary")
        network_add = request.form.get("network_add")
        wildcard_mask = request.form.get("wildcard_mask")
        ip_routes.add_eigrp_route(as_number,auto_summary,network_add,wildcard_mask)
        return Response(status=204)
    
@router_main.route('/routerOspfNetworkRouteConf', methods=['GET','POST'])
def conf_router_ospf_network_route():
    if request.method == 'POST':
        process_id = request.form.get("process_id")
        network_add = request.form.get("network_add")
        wildcard_mask = request.form.get("wildcard_mask")
        ospf_area = request.form.get("ospf_area")
        ip_routes.add_ospf_route(process_id,network_add,wildcard_mask,ospf_area)
        return Response(status=204)
    
@router_main.route('/routerOspfIntRouteConf', methods=['GET','POST'])
def conf_router_ospf_int_route():
    if request.method == 'POST':
        ospf_int = request.form.get("ospf_int")
        process_id = request.form.get("process_id")
        ospf_area = request.form.get("ospf_area")
        ip_routes.ospf_on_interface(ospf_int,process_id,ospf_area)
        return Response(status=204)


#Interface Configuration
@router_main.route('/routerConfIntLayerThree', methods=['GET','POST'])
def conf_router_int_layer_3():
    if request.method == 'POST':
        int_name = request.form.get("int_name")
        int_ip = request.form.get("int_ip")
        int_sub_mask = request.form.get("int_sub_mask")
        int_description = request.form.get("int_description")
        interface_config.configure_interface_layer_3(int_name,int_ip,int_sub_mask,int_description)
        return Response(status=204)
    
@router_main.route('/routerAddLoopbackInterface', methods=['GET','POST'])
def conf_loopback_int():
    if request.method == 'POST':
        loopb_number = request.form.get("loopb_number")
        interface_config.create_loopback_interface(loopb_number)
        return Response(status=204)

#LLDP configuration
@router_main.route('/routerLldpGlobalEnable', methods=['GET','POST'])
def router_lldp_global_enable():
    if request.method == 'POST':
        LLDP_config.LLDP_global_enable()
        return Response(status=204)
    
@router_main.route('/routerLldpIntEnable', methods=['GET','POST'])
def router_lldp_int_enable():
    if request.method == 'POST':
        lldp_interface = request.form.get("lldp_interface")
        LLDP_config.LLDP_interface_enable(lldp_interface)
        return Response(status=204)
    
@router_main.route('/routerLldpTimerConfig', methods=['GET','POST'])
def router_lldp_timer_config():
    if request.method == 'POST':
        timer_time = request.form.get("timer_time")
        LLDP_config.lldp_timer_config(timer_time)
        return Response(status=204)
    
@router_main.route('/routerLldpHoldtimeConfig', methods=['GET','POST'])
def router_lldp_holdtime_config():
    if request.method == 'POST':
        holdtime_time = request.form.get("holdtime_time")
        LLDP_config.lldp_holdtime_config(holdtime_time)
        return Response(status=204)
    
@router_main.route('/routerLldpReinitConfig', methods=['GET','POST'])
def router_lldp_reinit_config():
    if request.method == 'POST':
        reinit_time = request.form.get("reinit_time")
        LLDP_config.lldp_reinit_config(reinit_time)
        return Response(status=204)
    
#DNS configuration
@router_main.route('/routerAsDnsServerConfig', methods=['GET','POST'])
def router_dns_server_config():
    if request.method == 'POST':
        DNS_config.config_router_ip_dns()
        return Response(status=204)
    
@router_main.route('/addIpHostDnsConfig', methods=['GET','POST'])
def ip_host_dns_config():
    if request.method == 'POST':
        dns_hostname = request.form.get("dns_hostname")
        dns_ip = request.form.get("dns_ip")
        DNS_config.dns_add_ip_host(dns_hostname, dns_ip)
        return Response(status=204)
    
@router_main.route('/externalDnsServerConfig', methods=['GET','POST'])
def router_external_dns_server_config():
    if request.method == 'POST':
        dns_server_ip = request.form.get("dns_server_ip")
        DNS_config.ip_name_server(dns_server_ip)
        return Response(status=204)
    
@router_main.route('/domainLookupDnsConfig', methods=['GET','POST'])
def router_dns_query_config():
    if request.method == 'POST':
        DNS_config.perform_dns_queries()
        return Response(status=204)
    
@router_main.route('/setDomainNameConfig', methods=['GET','POST'])
def router_domain_name_config():
    if request.method == 'POST':
        domain_name = request.form.get("domain_name")
        DNS_config.set_domain_name(domain_name)
        return Response(status=204)


#DHCP configuration
@router_main.route('/dhcpExcludeAddress', methods=['GET','POST'])
def router_dhcp_exclude_address():
    if request.method == 'POST':
        exclude_start_ip = request.form.get("exclude_start_ip")
        exclude_end_ip = request.form.get("exclude_end_ip")
        DHCP_config.dhcp_exclude_address(exclude_start_ip,exclude_end_ip)
        return Response(status=204)
    
@router_main.route('/addDhcpPoolConfig', methods=['GET','POST'])
def router_add_dhcp_pool_config():
    if request.method == 'POST':
        pool_name = request.form.get("pool_name")
        pool_ip = request.form.get("pool_ip")
        pool_submask = request.form.get("pool_submask")
        DNS_server = request.form.get("DNS_server")
        domain_name = request.form.get("domain_name")
        default_router = request.form.get("default_router")
        DHCP_config.dhcp_pool(pool_name,pool_ip,pool_submask,DNS_server,domain_name,default_router)
        return Response(status=204)
    
@router_main.route('/routerDhcpRelayIntConfig', methods=['GET','POST'])
def router_dhcp_relay_int_config():
    if request.method == 'POST':
        relay_interface = request.form.get("relay_interface")
        interface_ip = request.form.get("interface_ip")
        DHCP_config.dhcp_relay_int(relay_interface,interface_ip)
        return Response(status=204)
    
@router_main.route('/routerDhcpClientInterfaceConfig', methods=['GET','POST'])
def router_dchp_client_int_config():
    if request.method == 'POST':
        client_interface = request.form.get("client_interface")       
        DHCP_config.dhcp_client_int(client_interface)
        return Response(status=204)
    
#router update os
@router_main.route('/routerUpdateOsConfig', methods=['GET','POST'])
def router_update_os_config():
    if request.method == 'POST':
        source = request.form.get("source")
        destination = request.form.get("destination")
        remote_host = request.form.get("remote_host")
        source_filename = request.form.get("source_filename")
        destination_filename = request.form.get("destination_filename")
        update_os.update_from_flash(source,destination, remote_host, source_filename, destination_filename)
        return Response(status=204)



#NTP configuration
@router_main.route('/routerSetClockConfig', methods=['GET','POST'])
def router_ntp_set_clock_config():
    if request.method == 'POST':
        hour = request.form.get("hour")
        minute = request.form.get("minute")
        second = request.form.get("second")
        day = request.form.get("day")
        month = request.form.get("month")
        year = request.form.get("year")
        NTP_config.set_clock(hour,minute,second,day,month,year)
        return Response(status=204)

@router_main.route('/routerSetCalendarConfig', methods=['GET','POST'])
def router_ntp_set_calendar_config():
    if request.method == 'POST':
        cal_hour = request.form.get("cal_hour")
        cal_minute = request.form.get("cal_minute")
        cal_second = request.form.get("cal_second")
        cal_day = request.form.get("cal_day")
        cal_month = request.form.get("cal_month")
        cal_year = request.form.get("cal_year")
        NTP_config.set_calendar(cal_hour,cal_minute,cal_second,cal_day,cal_month,cal_year)
        return Response(status=204)
    
@router_main.route('/routerReadCalendarConfig', methods=['GET','POST'])
def router_ntp_read_calendar_config():
    if request.method == 'POST':
        NTP_config.sync_clock_to_calendar()
        return Response(status=204)
    
@router_main.route('/routerUpdateCalendarConfig', methods=['GET','POST'])
def router_ntp_update_calendar_config():
    if request.method == 'POST':
        NTP_config.sync_calendar_to_clock()
        return Response(status=204)

@router_main.route('/routerTimezoneConfig', methods=['GET','POST'])
def router_ntp_timezone_config():
    if request.method == 'POST':
        timezone = request.form.get("timezone")
        hours = request.form.get("hours")
        minutes = request.form.get("minutes")
        NTP_config.set_clock_timezone_offset(timezone,hours,minutes)
        return Response(status=204)
    
@router_main.route('/routerSummerTimeConfig', methods=['GET','POST'])
def router_ntp_summertime_config():
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

@router_main.route('/routerAddNtpServer', methods=['GET','POST'])
def router_ntp_addserver_config():
    if request.method == 'POST':
        add_server_ntp = request.form.get("add_server_ntp")
        NTP_config.add_ntp_server(add_server_ntp)
        return Response(status=204)

@router_main.route('/routerNtpSourceLoopbackConfig', methods=['GET','POST'])
def router_ntp_source_loopback_config():
    if request.method == 'POST':
        loopback_int = request.form.get("loopback_int")
        NTP_config.add_ntp_source_loopback(loopback_int)
        return Response(status=204)

@router_main.route('/routerNtpMasterConfig', methods=['GET','POST'])
def router_ntp_master_config():
    if request.method == 'POST':
        NTP_config.ntp_master()
        return Response(status=204)

#VLAN Confid
@router_main.route('/routerCreateSubinterface', methods=['GET','POST'])
def router_add_vlan_subint():
    if request.method == 'POST':
        int_name = request.form.get("int_name")
        vlan_number = request.form.get("vlan_number")
        ip_address = request.form.get("ip_address")
        subnet_mask = request.form.get("subnet_mask")
        vlan_config.add_vlan_subinterfaces(int_name, vlan_number, ip_address, subnet_mask)
        return Response(status=204)
    
@router_main.route('/routerNativeVlanConfig', methods=['GET','POST'])
def router_add_native_vlan():
    if request.method == 'POST':
        sub_interface = request.form.get("sub_interface")
        native_vlan = request.form.get("native_vlan")
        vlan_config.router_add_native_vlan(sub_interface, native_vlan)
        return Response(status=204)








#SAVE and LOGOUT
@router_main.route('/routerSave')
def save():
    router_save_and_logout.router_save()
    return Response(status=204)
        

@router_main.route('/routerLogout')
def logout():
    #delete session info
    with current_app.app_context():
        mail = Mail()
        msg = Message(subject='configuration data from ' + session['user']['ip'], sender = 'NDMAS@BEproject.com', recipients = [session['user']['email']])
        msg.body = render_template("email.html",Device_data = tech_support.show_os_version_json(), SysLog = syslog.syslog_display())
        mail.send(msg)
        router_save_and_logout.router_logout()
        session.pop('user', None)
        return redirect(url_for("main"))

