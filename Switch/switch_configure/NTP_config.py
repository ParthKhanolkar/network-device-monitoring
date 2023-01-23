from connect import *

#manual time configuration
def set_clock():
    ssh_connect.enable()
    time = input("Enter time in hh:mm:ss format: ")
    day = input("Enter the day of the month: ")
    month = input("Enter the month of the year: ")
    year = input("Enter the year: ")
    ssh_connect.send_config_set(['clock set ' + day + ' ' + month + ' ' + year])

def set_calendar():
    ssh_connect.enable()
    time = input("Enter time in hh:mm:ss format: ")
    day = input("Enter the day of the month: ")
    month = input("Enter the month of the year: ")
    year = input("Enter the year: ")
    ssh_connect.send_config_set(['calendar set ' + day + ' ' + month + ' ' + year])

def sync_clock_to_calendar():
    ssh_connect.enable()
    ssh_connect.send_config_set(['clock read-calendar'])

def sync_calendar_to_clock():
    ssh_connect.enable()
    ssh_connect.send_config_set(['clock update-calendar'])

def set_clock_timezone_offset():
    ssh_connect.enable()
    timezone = input("Enter the timezone: ")
    hours = input("Enter hours offset from UTC: ")
    minutes = input("Enter minutes offset from UTC: ")
    ssh_connect.send_config_set(['clock timezone ' + timezone + ' ' + hours + ' ' + minutes])


def clock_summer_time_recurring_config():
    ssh_connect.enable()
    timezone = input("Enter the timezone: ")
    start_week_number = input("Enter the start week number: ")
    start_day = input("Enter the start day: ")
    start_month = input("Enter the start month: ")
    start_time = input("Enter the start time in hh:mm format: ")
    end_week_number = input("Enter the end week number: ")
    end_day = input("Enter the end day: ")
    end_month = input("Enter the end month: ")
    end_time = input("Enter the end time in hh:mm format: ")
    offset = input("Enter the offset in minutes: ")
    ssh_connect.send_config_set(['clock summer-time ' + timezone + ' recurring ' + start_week_number + ' ' + start_day + ' ' + start_month + ' ' + start_time + ' ' + end_week_number + ' ' + end_day + ' ' + end_month + ' ' + end_time + ' ' + offset])


#automatic time syncing
def add_ntp_server():
    ssh_connect.enable()
    add_server_ntp = input("Enter the IP address of the NTP server you want to add: ")
    ssh_connect.send_config_set(['ntp server ' + add_server_ntp])

def add_ntp_source_loopback():
    ssh_connect.enable()
    loopback_int = input("Enter Loopback interface: ")
    ssh_connect.send_config_set(['ntp source ' + loopback_int])

def ntp_master():
    ssh_connect.enable()
    ssh_connect.send_config_set(['ntp master'])


#ntp authentication