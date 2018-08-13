#! /usr/bin/env python3

import psutil
import monitor.varslist as v

ram = psutil.virtual_memory()
ram_percentage = float(ram.percent)

print('RAM used percentage is: ' + str(ram_percentage + '%'))

