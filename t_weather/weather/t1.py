#!/usr/bin/env python
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText

cmd = 'ifconfig'
m = os.popen(cmd)
t = m.read()
# 发送的为ifconfig命令执行的结果，没做其它处理
m.close()
msg = MIMEText(t, 'plain', 'utf-8')
msg['From'] = 'Raspberry'
msg['To'] = 'desticion'
msg['Subject'] = Header('Ip Address Report', 'utf-8').encode()
# 这里填发件地址
from_add = 'xxxx@xxxx.xx'
# 这里填目的地址
to_add = 'xxxx@qq.com'
# 这里填发件地址邮箱密码
password = 'xxx'
# 这里填发件邮箱smtp地址
smtp_sever = 'smtp.xxx.xx'
sever = smtplib.SMTP(smtp_sever, 25)
sever.set_debuglevel(1)
sever.login(from_add, password)
sever.sendmail(from_add, [to_add], msg.as_string())
sever.quit()
