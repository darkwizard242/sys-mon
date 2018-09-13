[![Build Status](https://travis-ci.com/Tech-Overlord/sys-mon.svg?branch=master)](https://travis-ci.com/Tech-Overlord/sys-mon)   [![license](https://img.shields.io/badge/license-BSD%202--Clause-blue.svg)](https://github.com/Tech-Overlord/sys-mon/blob/master/LICENSE.md)
# sys-mon:

Utility being developed in Python purely for the purposes of resource monitoring and alert system.

## Key Features:
 1. Consistent RAM utilization monitoring. 
    * Define a threshold limit, for e.g. 70% .
    * Program will perform multiple actions when the RAM utilization exceeds the threshold.
 2. Report File generation.
    * Generates report in a .txt format. Obviously can change it to any other extension if need be like ".log".
    * Report file will contain the exact time, date along with the defined threshold and the utilization identified when exceeded.
    * Will also print the Total, Used & Free RAM.
 3. Archiving Report file.
    * Report file will be deflated and archived for housekeeping purposes.
 4. Email alert to the owner with report archive as an attachment.
    * Use of python smtpblib library to connect with Gmail's SMTP server and send an outgoing email to the owner which will also include attachment of the archive.