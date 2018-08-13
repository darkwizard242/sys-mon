#! /usr/bin/env python3

import smtplib

# SMTP object that represents connection to a SMTP server. This is connecting using SSL.
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# Confirming connection with SMTP Server.
smtpObj.ehlo()


# STMP login details. Email & Password.
smtpObj.login( 'senderemail@gmail.com', '*******')

# Sending email. First is the FROM address, second is the TO address followed by Subject and message in new line.
smtpObj.sendmail('senderemail@gmail.com', 'receiver email@gmail.com', 'Subject: Hi again!.\nThis is a test email')

# Exiting SMTP connection.
smtpObj.quit()
