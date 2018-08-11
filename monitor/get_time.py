#! /usr/bin/env python3

import datetime

d = datetime.datetime.now()

print('Threshold limit recorded at: ')
print(d.strftime('Date: ' + '%d/%m/%Y'))
print(d.strftime('Date: ' + '%B %d, %Y'))
print(d.strftime('Day: ' + '%A'))
print(d.strftime('Time: ' + '%H:%M:%S %p'))
