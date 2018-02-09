#!/usr/bin/env python
# -*- coding:utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib

def _format_add(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEMultipart('alternative')
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()
msg['From'] = _format_add('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_add('yushuo <%s>' % to_addr)

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' + 
    '<p><img src="cid:0"></p>' + 
    '</body></html>', 'html', 'utf-8'))

with open('./dogyear.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='dogyear.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='dogyear.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-ID', '0')

    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

#server = smtplib.SMTP(smtp_server, 25)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()