import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time


def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'xxx@qq.com'
    msg['To'] = 'xxx@qq.com'

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


bsObj = BeautifulSoup(urlopen('http://isitchristmas.com/'), 'html.parser')
while bsObj.find('a', {'id', 'answer'}.attrs['title'] == '不是'):
    print('It is not Christmas yet.')
    time.sleep(3600)
    bsObj = BeautifulSoup(urlopen('http://isitchristmas.com/'))
sendMail("It's Christmas!", "According to http://itischristmas, it is Christmas!")