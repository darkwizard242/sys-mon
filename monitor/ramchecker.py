#! /usr/bin/env python3

import monitor.varslist as v
import monitor.filegenerator as fg


def ram_check():
    if v.ram_percentage >= v.threshold:
        print('RAM usage has exceeded the specified threshold, which is: ' + str(v.threshold) + '%')
        print('Current RAM usage is: ' + str(v.ram_percentage) + '%')
        fg.win_folder()
    else:
        print("RAM usage is under threshold limit.")


ram_check()
