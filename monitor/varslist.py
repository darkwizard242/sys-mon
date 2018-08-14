#! /usr/bin/env python3

import datetime
import psutil


# Defining data measurements
bit = 0 or 1
byte = float(8)
kilobyte = float(1024)
megabyte = float(1024 * 1024)
gigabyte = float(1024 * 1024 * 1024)


# Assigning variable for the type of data measurement to be used throughout the program.
data_measure = gigabyte


# Variables around RAM usage.
memory = psutil.virtual_memory()
# Total Memory variables.
memory_kb_total = float(memory.total/kilobyte)
memory_mb_total = float(memory.total/megabyte)
memory_gb_total = float(memory.total/gigabyte)
# Free Memory variables.
memory_kb_free = float(memory.free/kilobyte)
memory_mb_free = float(memory.free/megabyte)
memory_gb_free = float(memory.free/gigabyte)
# Used Memory variables.
memory_kb_used = float(memory.used/kilobyte)
memory_mb_used = float(memory.used/megabyte)
memory_gb_used = float(memory.used/gigabyte)
# Used Memory Percent Variable.
ram_percentage = float(memory.percent)


# Set RAM Threshold
threshold = float(50)

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