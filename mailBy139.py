# -*- coding: utf-8 -*-
import smtplib  
from email.mime.text import MIMEText  
_user = "*************@139.com"  
_pwd  = "************"  
_to   = "**********@139.com"  
  
#ʹ��MIMEText�������smtpЭ���header��body  
msg = MIMEText("��װ���,�����ֶ�")  
msg["Subject"] = "don't panic"  
msg["From"]    = _user  
msg["To"]      = _to  
  
s = smtplib.SMTP("smtp.139.com", timeout=30)#����smtp�ʼ�������,�˿�Ĭ����25  
s.login(_user, _pwd)#��½������  
s.sendmail(_user, _to, msg.as_string())#�����ʼ�  
s.close()  

