#! /usr/bin/env python3

import datetime

# Defining data measurements
bit = 0 or 1
byte = float(8)
kilobyte = float(1024)
megabyte = float(1024 * 1024)
gigabyte = float(1024 * 1024 * 1024)


# Variable for winfolder method
win_dir = str('D:\\Monitory_Reports\\')


# Assigning value of datetime module's datetime function to variable 'd' and other strings for filename's
# timestamp association.
d = datetime.datetime.now()
d_date_report_filename = d.strftime('%d%m%Y')
d_day_report_filename = d.strftime('%A')
d_time_report_filename = d.strftime('%H%M%S')


# Assigning value of datetime module's datetime function to variable 'd' and other strings for associating file's
# input.
d_date_report_input = d.strftime('%B %d, %Y')
d_day_report_input = d.strftime('%A')
d_time_report_input = d.strftime('%I:%M:%S %p')
# Assigning a variable for printing incident record time.
incident_record = str('Incident recorded at:')