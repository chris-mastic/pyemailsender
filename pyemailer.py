#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 03:58:54 2020

@author: tech
"""

import smtplib#to create an smtp server
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Me'
email['to'] = 'clmaz031882@gmail.com'
email['subject'] = 'You won a million dollars'

email.set_content(html.substitute({'name':'TinTin'}),'html')#could be text, html, images

#use smtp server to log into our gmail client and send our email
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()#an encryption method
    smtp.login('clmaz031882@gmail.com','chris_mazza_16602134')
    smtp.send_message(email)
    print('all good  thoughts')
