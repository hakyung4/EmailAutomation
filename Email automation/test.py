#This file is for getting my email checked before I send it out to parents.
import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDR = os.environ.get('EMAIL_ADDR')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

contacts = ['klskoreanlanguage@gmail.com']

msg = EmailMessage()
msg['Subject'] = '11/13 Saturday Class'
msg['From'] = EMAIL_ADDR
msg['To'] = ', '.join(contacts)

msg.add_alternative("""\
<!DOCTYPE html>
<html>
<body>
    <h3><b>안녕하세요!</b></h3>
    <p>This is Peter Yun, this year's ESL 1 teacher. Last Saturday, students learned about fictional texts and how to distinguish them from facts and nonfictions. I would appreiciate it if all students brought the following items to school:</p>
    <ul>
        <li>Pencils</li>
        <li>Eraser</li>
        <li>Water bottle</li>
    </ul>
    <p>This Saturday, students will demonstrate their knowledge they have gained through a final exam. Subsequently, they will learn the fundamentals of non-fictions.</p>
    <p>--------------------------------------------------------------------------------------------------------------------------------------------------------</p>
    <ol>
        <li>10:30-11:20-> <b>Taking a final exam</b></li>
        <ol>
            <li>Final exam</li>
        </ol>
        <li>11:20-12:10-> <b>Non-fictions</b></li>
        <ol>
            <li>Vocabulary Practice: Non-fiction Genre</li>
            <li>Soccer: Nonfiction Text</li>
        </ol>
        <li>12:10-12:30-> <b>Snack</b></li>
        <ol>
            <li>dunkin donuts</li>
            <li>Milk</li>
        </ol>
        <li>12:30-1:30-> <b>Collaborative activities</b></li>
        <ol>
            <li>Volleyball with balloons</li>
            <li>Pictonary</li>
        </ol>
    </ol>
    <p>--------------------------------------------------------------------------------------------------------------------------------------------------------</p>
    <h3><b>Ways to contact me:</b></h3>
    <p>--------------------------------------------------------------------------------------------------------------------------------------------------------</p>
    <p>My email- hamiram9@gmail.com</p>
    <p>My Phone- (217)417-2802</p>
    <p>카톡- yhk420</p>
    <p>--------------------------------------------------------------------------------------------------------------------------------------------------------</p>
    <p>교감 김지수: 217-419-4257</p>
    <p>교장 이유리: 217-766-0988</p>
    <p>한글학교 이메일: klskoreanlanguage@gmail.com</p>
    <p>Best,</p>
    <p>Peter Yun</p>
</body>
</html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDR, EMAIL_PASS)

    
    smtp.send_message(msg)