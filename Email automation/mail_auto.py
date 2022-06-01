#This is the one that gets sent to parents.
import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDR = os.environ.get('EMAIL_ADDR')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

contacts = ['']

msg = EmailMessage()
msg['Subject'] = ''
msg['From'] = EMAIL_ADDR
msg['To'] = ', '.join(contacts)

msg.add_alternative("""\
<!DOCTYPE html>
<html>
<body>
    
</body>
</html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDR, EMAIL_PASS)

    
    smtp.send_message(msg)
    
