from netmiko import ConnectHandler

#manual time configuration
def set_clock(hour,minute,second,day,month,year):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_command(f"clock set {hour}:{minute}:{second} {day} {month} {year}")

def set_calendar(cal_hour,cal_minute,cal_second,cal_day,cal_month,cal_year):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_command(f"calendar set {cal_hour}:{cal_minute}:{cal_second} {cal_day} {cal_month} {cal_year}")

def sync_clock_to_calendar():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_command('clock read-calendar')

def sync_calendar_to_clock():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_command('clock update-calendar')

def set_clock_timezone_offset(timezone,hours,minutes):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set([f"clock timezone {timezone} {hours} {minutes}"])


def clock_summer_time_recurring_config(timezone,start_week_number,start_day,start_month,start_hour,start_minute,end_week_number,end_day,end_month,end_hour,end_minute,offset):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set([f"clock summer-time {timezone} recurring {start_week_number} {start_day} {start_month} {start_hour}:{start_minute} {end_week_number} {end_day} {end_month} {end_hour}:{end_minute} {offset}"])


#automatic time syncing
def add_ntp_server(add_server_ntp):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ntp server ' + add_server_ntp])

def add_ntp_source_loopback(loopback_int):
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ntp source ' + loopback_int])

def ntp_master():
    from connect import get_ssh_connect
    ssh_connect = get_ssh_connect()
    ssh_connect.enable()
    ssh_connect.send_config_set(['ntp master'])


#ntp authentication