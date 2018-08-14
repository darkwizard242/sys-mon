#! /usr/bin/env python3

import psutil
import monitor.varslist as v

def ram_check():
    ram = psutil.virtual_memory()
    ram_percentage = float(ram.percent)
    threshold = float(50)
    if ram_percentage >= threshold:
        print('RAM usage has exceeded the specified threshold, which is: ' + str(threshold) + '%')
        print('Current RAM usage is: ' + str(ram_percentage) + '%')
    else:
        print("RAM usage is under threshold limit.")

ram_check()


