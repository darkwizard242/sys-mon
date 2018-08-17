#! /usr/bin/env python3

import monitor.varslist as v
import monitor.filegenerator as fg


def ram_check():
    """
    IF/ELSE statements to verify whether the current RAM utilization exceeds the specified threshold.
    IF RAM utilization exceeds than the threshold, then print the utilization recorded, along with threshold and then
    call the function win_folder() from monitor.filegenerator module.
    Else a message is printed suggesting that the RAM usage is under the specified threshold.
    """
    if v.ram_percentage >= v.threshold:
        print('RAM usage has exceeded the specified threshold, which is: ' + str(v.threshold) + '%')
        print('Current RAM usage is: ' + str(v.ram_percentage) + '%')
        fg.win_folder()
        fg.win_archive_report()
    else:
        print("RAM usage is under threshold limit.")


# ram_check()
