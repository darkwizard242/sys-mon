#! /usr/bin/env python3

import datetime
import os
import monitor.varslist as v
import monitor.archiver as arch


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


def win_folder():
    """
    IF Statement verifies whether the directory specified against variable 'win_dir' exists or not.

    IF exists, then generate a couple of print statements.

        use of os functions for opening (or creating a file if it doesn't exist) based on the value of
        v.win_report_file_explicit.

        Prints the threshold limit set by the user.

        Prints the current RAM limit i.e. the exceeded limit.

        Nested IF/ELSE verifies what the data measurement type variable's value is & depending on that performs the
        following:
            1. Prints Total RAM.
            2. Prints Current Used RAM.
            3. Prints Current Free RAM.

    Else, creates the directory and then generates a couple of print statements followed by the following actions:

        use of os functions for opening (or creating a file if it doesn't exist) based on the value of
        v.win_report_file_explicit.

        Prints the threshold limit set by the user.

        Prints the current RAM limit i.e. the exceeded limit.

        Nested IF/ELSE verifies what the data measurement type variable's value is & depending on that performs the
        following:
            1. Prints Total RAM.
            2. Prints Current Used RAM.
            3. Prints Current Free RAM.

    :return:
    """
    if os.path.exists(v.win_dir):
        print('Directory where reports are generated already exists. No new directory will be created.')
        print('Report Generation directory path is: ' + v.win_dir)
        print('Generated Report file is: ' + str(v.win_report_file_explicit))
        thewriter = open(v.win_report_file, 'a')
        thewriter.write(v.incident_record)
        thewriter.write('\nDirectory is: ' + v.win_dir)
        thewriter.write('\nIncident Date: ' + v.d_date_report_input)
        thewriter.write('\nIncident Time of record: ' + v.d_time_report_input)
        thewriter.write('\nRAM usage has exceeded the specified threshold, which is: ' + str(v.threshold) + '%')
        thewriter.write('\nExceeded RAM record usage is: ' + str(v.ram_percentage) + '%')
        if v.data_measure == v.kilobyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_kb_total) + ' KBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_kb_used) + ' KBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_kb_free) + ' KBs')
        elif v.data_measure == v.megabyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_mb_total) + ' MBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_mb_used) + ' MBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_mb_free) + ' MBs')
        elif v.data_measure == v.gigabyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_gb_total) + ' GBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_gb_used) + ' GBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_gb_free) + ' GBs')
        else:
            print("Please correct the data_measurement variable value in varslist.")
    else:
        print('Directory where reports are generated does not exist and will now be created.')
        os.makedirs(v.win_dir, exist_ok=True)
        print('Report Generation directory has been created on: ' + v.win_dir)
        print('Generated Report file is: ' + str(v.win_report_file_explicit))
        thewriter = open(v.win_report_file, 'a')
        thewriter.write(v.incident_record)
        thewriter.write('\nDirectory is: ' + v.win_dir)
        thewriter.write('\nIncident Date: ' + v.d_date_report_input)
        thewriter.write('\nIncident Time of record: ' + v.d_time_report_input)
        thewriter.write('\nRAM usage has exceeded the specified threshold, which is: ' + str(v.threshold) + '%')
        thewriter.write('\nExceeded RAM record usage is: ' + str(v.ram_percentage) + '%')
        if v.data_measure == v.kilobyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_kb_total) + ' KBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_kb_used) + ' KBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_kb_free) + ' KBs')
        elif v.data_measure == v.megabyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_mb_total) + ' MBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_mb_used) + ' MBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_mb_free) + ' MBs')
        elif v.data_measure == v.gigabyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_gb_total) + ' GBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_gb_used) + ' GBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_gb_free) + ' GBs')
        else:
            print("Please correct the data_measurement variable value in varslist.")


def call_archive():
    arch.win_archive_report()   # Call to windows archiving function.


# def win_archive_report():
#     os.chdir(v.win_dir)
#     print('Current directory is: ' + os.getcwd())
#     v.archive_proc.write(v.file_to_archive, compress_type=v.zipfile.ZIP_DEFLATED)
#     v.archive_proc.close()


def linux_folder():
    os.makedirs(v.nix_dir, exist_ok=True)
    if os.path.exists(v.nix_dir):
        print('Directory where reports are generated already exists. No new directory will be created.')
        print('Report Generation directory path is: ' + v.nix_dir)
        print('Generated Report file is: ' + str(v.nix_report_file_explicit))
        os.chdir(v.nix_dir)
        thewriter = open(v.nix_report_file, 'a')
        thewriter.write(v.incident_record)
        thewriter.write('\nDirectory is: ' + v.nix_dir)
        thewriter.write('\nIncident Date: ' + v.d_date_report_input)
        thewriter.write('\nIncident Time of record: ' + v.d_time_report_input)
        thewriter.write('\nRAM usage has exceeded the specified threshold, which is: ' + str(v.threshold) + '%')
        thewriter.write('\nExceeded RAM record usage is: ' + str(v.ram_percentage) + '%')
        if v.data_measure == v.kilobyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_kb_total) + ' KBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_kb_used) + ' KBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_kb_free) + ' KBs')
        elif v.data_measure == v.megabyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_mb_total) + ' MBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_mb_used) + ' MBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_mb_free) + ' MBs')
        elif v.data_measure == v.gigabyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_gb_total) + ' GBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_gb_used) + ' GBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_gb_free) + ' GBs')
        else:
            print("Please correct the data_measurement variable value in varslist.")
    else:
        print('Directory where reports are generated does not exist and will now be created.')
        os.makedirs(v.nix_dir, exist_ok=True)
        print('Report Generation directory has been created on: ' + v.nix_dir)
        print('Generated Report file is: ' + str(v.nix_report_file_explicit))
        os.chdir(v.nix_dir)
        thewriter = open(v.nix_report_file, 'a')
        thewriter.write(v.incident_record)
        thewriter.write('\nDirectory is: ' + v.nix_dir)
        thewriter.write('\nIncident Date: ' + v.d_date_report_input)
        thewriter.write('\nIncident Time of record: ' + v.d_time_report_input)
        thewriter.write('\nRAM usage has exceeded the specified threshold, which is: ' + str(v.threshold) + '%')
        thewriter.write('\nExceeded RAM record usage is: ' + str(v.ram_percentage) + '%')
        if v.data_measure == v.kilobyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_kb_total) + ' KBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_kb_used) + ' KBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_kb_free) + ' KBs')
        elif v.data_measure == v.megabyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_mb_total) + ' MBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_mb_used) + ' MBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_mb_free) + ' MBs')
        elif v.data_measure == v.gigabyte:
            thewriter.write('\nTotal RAM is: ' + str(v.memory_gb_total) + ' GBs')
            thewriter.write('\nUsed RAM recorded: ' + str(v.memory_gb_used) + ' GBs')
            thewriter.write('\nFree RAM recorded: ' + str(v.memory_gb_free) + ' GBs')
        else:
            print("Please correct the data_measurement variable value in varslist.")
