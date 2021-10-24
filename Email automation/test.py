#This file is for getting my email checked before I send it out to parents.
import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDR = os.environ.get('EMAIL_ADDR')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

contacts = ['hakyung4@illinois.edu']
# contacts = ['klskoreanlanguage@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'You'
msg['From'] = EMAIL_ADDR
msg['To'] = ', '.join(contacts)

msg.add_alternative("""\
<!DOCTYPE html>
<html>
<body>
    <h3><b>안녕하세요!</b></h3>
    <p>This is Peter Yun, this year's ESL 1 teacher. Since this week is halloween week, students are welcome to bring or put on whatever they want to wear; however, I highly encourage everyone to bring their own jacket in case we go outside for activities. I would appreiciate it if all students brought the following items to school:</p>
    <ul>
        <li>Pencils</li>
        <li>Eraser</li>
        <li>Water bottle</li>
    </ul>
    <p>This Saturday, students will learn Point of view in stories and practice identifying it.</p>
    <p>--------------------------------------------------------------------------------------------------------------------------------------------------------</p>
    <ol>
        <li>10:30-11:20-> <b>Point of view</b></li>
        <ol>
            <li>Point of view</li>
            <li>Pronouns & Point of View</li>
        </ol>
        <li>11:20-12:10-> <b>Exercise</b></li>
        <ol>
            <li>Point of view in sentences</li>
            <li>Practicing point of view</li>
        </ol>
        <li>12:10-12:30-> <b>Snack</b></li>
        <ol>
            <li>Ham & Cheese croissant sandwhich</li>
            <li>Orange juice</li>
        </ol>
        <li>12:30-1:30-> <b>Collaborative activities</b></li>
        <ol>
            <li>Making Dalgona</li>
            <li>Making Ddakji</li>
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