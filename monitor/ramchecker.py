#! /usr/bin/env python3

import monitor.varslist as v
import monitor.filegenerator as fg
import monitor.archiver as arc


def ram_check():
    """
    IF/ELSE statements to verify whether the current RAM utilization exceeds the specified threshold.

    IF RAM utilization exceeds than the threshold, then check the os type.
        1. IF OS type is 'Windows', print the utilization recorded, along with threshold and then
        call the function win_folder() from monitor.filegenerator module. Call to archiving function after that.

        2. ELSE IF OS type is 'Linux', print the utilization recorded, along with threshold and then
        call the function linux_folder() from monitor.filegenerator module. Call to archiving function after that.

        3. ELSE print that the OS is unsupported.

    Else a message is printed suggesting that the RAM usage is under the specified threshold.
    """
    if v.ram_percentage >= v.threshold:
        if v.os_type == 'Windows':
            print('System is Windows.')
            print('RAM usage has exceeded the specified threshold, which is: ' + str(v.threshold) + '%')
            print('Current RAM usage is: ' + str(v.ram_percentage) + '%')
            fg.win_folder()
            arc.win_archive_report()
        elif v.os_type == 'Linux':
            print('System is Linux.')
            print('RAM usage has exceeded the specified threshold, which is: ' + str(v.threshold) + '%')
            print('Current RAM usage is: ' + str(v.ram_percentage) + '%')
            fg.linux_folder()
            arc.nix_archive_report()
        else:
            print("Not a supported OS Type")
    else:
        print("RAM usage is under threshold limit.")


# ram_check()
