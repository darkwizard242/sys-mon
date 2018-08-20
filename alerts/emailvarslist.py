#! /usr/bin/env python3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import monitor.varslist as v

# Variables for SMTP connection details such as SMTP URL and SMTP PORT
smtp_url = 'smtp.gmail.com'
smtp_port = 465

# Variables for Sender's Email & Password
sender_email = str('sender0@gmail.com')
sender_password = str('password')

# Variable for Receiver's Email.
receiver_email = str('receiver@gmail.com')

#
subject = str("URGENT: RAM limit exceeded")
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
body = str('\nIncident Time of record: ' + v.d_time_report_input + '\n' + '\nTotal RAM is: ' + str(v.memory_gb_total)
           + ' GBs\n' + '\nUsed RAM recorded: ' + str(v.memory_gb_used) + ' GBs\n' + '\nFree RAM recorded: '
           + str(v.memory_gb_free) + ' GBs\n')
message.attach(MIMEText(body, 'plain'))
text = message.as_string()

# Gmail's link to enable use by less secure apps.
# https://myaccount.google.com/lesssecureapps?pli=1
