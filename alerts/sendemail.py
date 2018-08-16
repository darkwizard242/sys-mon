#! /usr/bin/env python3

import smtplib
import alerts.emailvarslist as ev

# SMTP object that represents connection to a SMTP server. This is connecting using SSL.
smtpObj = smtplib.SMTP_SSL(ev.smtp_url, ev.smtp_port)

# Confirming connection with SMTP Server.
smtpObj.ehlo()


# STMP login details. Email & Password.
smtpObj.login(ev.sender_email, ev.sender_password)

# Sending email. First is the FROM address, second is the TO address followed by Subject and message in new line.
smtpObj.sendmail(ev.sender_email, ev.receiver_email, 'Subject: Hi again!.\nThis is a test email')

# Exiting SMTP connection.
smtpObj.quit()
