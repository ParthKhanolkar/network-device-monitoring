from flask import Flask, Blueprint, redirect, url_for, render_template, request, flash, session, json, jsonify, Response

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

import Router.router_save_logout.router_save_and_logout as router_save_and_logout





@router_main.route("/router")
def home():
    if('user' in session):
        return render_template("router_main.html",hoverData=hover_info_display.display_info_on_hover(), deviceInterfaces=interfaces_display.grab_interfaces())
    else:
        return redirect(url_for("main"))

#Display------------------------------------------------------------------------------------------
#configuration_display
@router_main.route("/routerRunConf")
def disp_router_run_conf():
    #if request.method == 'POST':
    #datavar = jsonify(request.form)
    #print(datavar)
    #html_item = json.dumps(request.form, indent=2, separators=(', ', ': '))
    #print(html_item)
    #return('',204)
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
        #print(['interface ' + ospf_int, 'ip ospf ' + process_id + ' ' + 'area ' + ospf_area])
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

@router_main.route('/routerSave')
def save():
    router_save_and_logout.router_save()
    return Response(status=204)
        

@router_main.route('/routerLogout')
def logout():
    #delete session info
    router_save_and_logout.router_logout()
    session.pop('user', None)
    return redirect(url_for("main"))

