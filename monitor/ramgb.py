#! /usr/bin/env python3

import monitor.varslist as v


# Defining function ram_specs that uses modules/functions from psutil library and from variables_data.
def ram_specs():
        print()
        print('Total memory is: ' + str(float(v.memory_gb_total)) + ' GBs')
        print('Current available memory is: ' + str(float(v.memory_gb_free)) + ' GBs')
        print('Current used memory is: ' + str(float(v.memory_gb_used)) + ' GBs')
        print('Percentage of RAM being utilized currently: ' + str(float(v.ram_percentage)) + '%')


# ram_specs()
