#!C:\Users\asus\Desktop
# coding=gbk

import smtplib
from email.mime.text import MIMEText
#���÷�����������Ϣ
#163�����������ַ
mail_host = 'smtp.163.com'  
#163�û���
mail_user = 'xxx@163.com'  
#����(��������Ϊ��Ȩ��) 
mail_pass = 'xxx'   
#�ʼ����ͷ������ַ
sender = 'xxx@163.com'  
#�ʼ����ܷ������ַ��ע����Ҫ[]����������ζ�������д����ʼ���ַȺ��
receivers = ['xxx@qq.com']  

content="��ã����ǽ�������"

#����email��Ϣ
#�ʼ���������
message = MIMEText(content,'plain','utf-8')
#�ʼ�����       
message['Subject'] = '���ҽ���' 
#���ͷ���Ϣ
message['From'] = sender 
#���ܷ���Ϣ     
message['To'] = receivers[0]  

#��¼�������ʼ�
try:
    smtpObj = smtplib.SMTP() 
    #���ӵ�������
    smtpObj.connect(mail_host,25)
    #��¼��������
    smtpObj.login(mail_user,mail_pass) 
    #����
    smtpObj.sendmail(
        sender,receivers,message.as_string()) 
    #�˳�
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e)