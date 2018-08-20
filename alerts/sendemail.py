#! /usr/bin/env python3

import smtplib
import alerts.emailvarslist as ev


# SMTP object that represents connection to a SMTP server. This is connecting using SSL.
server = smtplib.SMTP_SSL(ev.smtp_url, ev.smtp_port)

# Confirming connection with SMTP Server.
server.ehlo()


# STMP login details. Email & Password.
server.login(ev.sender_email, ev.sender_password)


# Sending email. First is the FROM address, second is the TO address followed by Subject and message in new line.
server.sendmail(ev.sender_email, ev.receiver_email, ev.text)

# Exiting SMTP connection.
server.quit()
