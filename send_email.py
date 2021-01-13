import smtplib
from email.message import EmailMessage
from typing import ByteString
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Aime Malaika'
email['to'] = 'aimemalaika1995@gmail.com'
email['subject'] = 'You wan 1000000 dollars!'

email.set_content(html.substitute({'name':'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('acontrol08@gmail.com','aime1995')
    smtp.send_message(email)
    print('sent')
    