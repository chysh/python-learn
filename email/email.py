#!/etc/bin/python
# -*- utf:utf-8 -*-

from email.mime.text import MIMEText
from email.header import Header
import smtplib
msg = MIMEText('浮生若梦，为欢几何', 'plain', 'utf-8')

from_addr = input('From: ')
password = input('Password: ')

to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg['Subject'] = Header('时间', 'utf-8').encode()
msg['from'] = from_addr
msg['to'] = to_addr

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
