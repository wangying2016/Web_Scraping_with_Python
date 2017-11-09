import smtplib
from email.mime.text import MIMEText

msg = MIMEText('The body of the email is here')

msg['Subject'] = 'An Email Alert'
msg['From'] = 'xxx@qq.com'
msg['To'] = 'yyy@outlook.com'

s = smtplib.SMTP_SSL('smtp.qq.com', 465)
s.login('xxx@qq.com', 'zzz')
s.send_message(msg)
s.quit()
