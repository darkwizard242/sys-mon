#! /usr/bin/env python3

import monitor.varslist as v


# Defining function ram_specs that uses modules/functions from psutil library and from variables_data.
def ram_specs():
    # Set flow based on Threshold value.
        print()
        print('Total memory is: ' + str(float(v.memory_kb_total)) + ' KBs')
        print('Current available memory is: ' + str(float(v.memory_kb_free)) + ' KBs')
        print('Current used memory is: ' + str(float(v.memory_kb_used)) + ' KBs')
        print('Percentage of RAM being utilized currently: ' + str(float(v.ram_percentage)) + '%')


# ram_specs()
