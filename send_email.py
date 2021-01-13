import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Aime Malaika'
email['to'] = 'aimemalaika1995@gmail.com'
email['subject'] = 'You wan 1000000 dollars!'

email.set_content('I am a python student!')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('acontrol08@gmail.com','aime1995')
    smtp.send_message(email)
    print('sent')
    