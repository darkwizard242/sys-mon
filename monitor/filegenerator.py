#! /usr/bin/env python3

import datetime
import os
import varslist as v

def fetch_time():
    """
    This function imports the current time details for both date and time.
    strftime() method from datetime module allows displaying the date & time in string format.

    strftime()strings       Meaning
    %Y                      YEAR will be displayed as the century i.e. '2018'
    %y                      YEAR will be displayed without the century i.e. '18'
    %m                      MONTH will be displayed as decimal number from '01' to '12'
    %B                      MONTH will be displayed with full name i.e. 'August'
    %b                      MONTH will be displayed in abbreviated form i.e. 'Aug'
    %d                      DAY of the MONTH will be displayed in numeric form i.e. from '01' to '31'
    %j                      DAY of the YEAR will be displayed in numeric form i.e. from '001' to '366'
    %w                      DAY of the WEEK will be displayed in numeric form i.e. from '0'(Sunday) to '6'(Saturday).
    %A                      DAY of the WEEK will be displayed in alphabetic form i.e. 'Sunday'
    %a                      DAY of the WEEK will be displayed in abbreviated form i.e. 'Sun'
    %H                      HOUR will be displayed in 24 hours clock numeric form i.e. '00' to '23'.
    %I                      HOUR will be displayed in 12 hours clock numeric form i.e. '01' to '12'.
    %M                      MINUTES will be displayed in numeric form i.e. '00' to '59'.
    %S                      SECONDS will be displayed in numeric form i.e. '00' to '59'.
    %p                      HOUR MERIDIEM will be displayed in alphabetic form i.e. 'AM' or 'PM'.

    For both date and time outputs, format can be re-arranged by modifying the custom string.
    Date can be printed in numerical or alphanumerics values.
    Day is printed with an alphabetical value.
    Time is also printed in numeric format starting with HOUR:MINUTES:SECONDS

    :return: str
    """
    # Assigning value of datetime module's datetime function to variable 'd'.
    d = datetime.datetime.now()
    d_date = d.strftime('%B %d, %Y')
    d_day = d.strftime('%A')
    d_time = d.strftime('%I:%M:%S %p')
    incident_record = str('Incident recorded at:')
    print('Threshold limit recorded at: ')
    print(d_date)
    print(d_day)
    print(d_time)
    return d, d_date, d_day, d_time


def win_folder():
    if os.path.exists(v.directory):
        print('Directory where reports are generated already exists. No new directory will be created.')
        print('Report Generation directory path is: ' + v.directory)
        report_file = (v.directory + 'report_' + v.d_date_report_filename + '-' + v.d_time_report_filename + '.txt')
        thewriter = open(report_file, 'a')
        thewriter.write(v.incident_record)
        thewriter.write('\nDirectory is: ' + v.directory)
        thewriter.write('\nIncident Date: ' + v.d_date_report_input)
        thewriter.write('\nIncident Time of record: ' + v.d_time_report_input)
    else:
        print('Directory where reports are generated does not exist and will now be created.')
        os.makedirs(v.directory, exist_ok=True)
        print('Report Generation directory has been created on: ' + v.directory)
        report_file = (v.directory + 'report_' + v.d_date_report_filename + '-' + v.d_time_report_filename + '.txt')
        thewriter = open(report_file, 'a')
        thewriter.write(v.incident_record)
        thewriter.write('\nDirectory is: ' + v.directory)
        thewriter.write('\nIncident Date: ' + v.d_date_report_input)
        thewriter.write('\nIncident Time of record: ' + v.d_time_report_input)


def linux_folder():
    directory = str('D:\\Monitory_Reports')
    os.makedirs(directory, exist_ok=True)


#print(fetch_time.__doc__)
#fetch_time()

#help(fetch_time())
