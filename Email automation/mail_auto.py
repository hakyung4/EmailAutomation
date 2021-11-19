#This is the one that gets sent to parents.
import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDR = os.environ.get('EMAIL_ADDR')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

contacts = ['angtal82@gmail.com', 'rtxcorp@nate.com', '7942ar@gmail.com', 'miracle00827@gmail.com']

msg = EmailMessage()
msg['Subject'] = '11/20 Saturday Class'
msg['From'] = EMAIL_ADDR
msg['To'] = ', '.join(contacts)

msg.add_alternative("""\
<!DOCTYPE html>
<html>
<body>
    <h3><b>안녕하세요!</b></h3>
    <p>This is Peter Yun, this year's ESL 1 teacher. As this Saturday will be the last day of my teaching, I would personally like to thank you all for giving me an awesome opportunity to teach your children. As an ESL teacher, I remember the time when I was not fluent in English; I could barely understand or talk in English. However, I tried to listen to my friends and mock the phrases they say or accent they make, ultimately helping me become more than fluent in English. My advice for learning English, or any other foreign language is confidence. Keep encouraging your children to speak English and not to lose their confidence! I believe they will feel more than comfortable communicating in English one day!
    Other than this massmail, there is an email sent to each parents with students' certificates and feedbacks from me. Again, it was my pleasure to get to teach phenomenal students this year!</p> 
    <p>This Saturday, we are going to watch the first series of Harry Potter, Harry Potter and the Sorcerer's Stone</p>
    <p>--------------------------------------------------------------------------------------------------------------------------------------------------------</p>
    <ol>
        <li>10:30-11:20-> <b>Watching the movie</b></li>
        <ol>
            <li>Harry Potter and the Sorcerer's Stone</li>
        </ol>
        <li>12:10-12:30-> <b>Snack</b></li>
        <ol>
            <li>Chicken Nuggets</li>
            <li>Orange Juice</li>
        </ol>
        <li>12:30-1:30-> <b>Collaborative activities</b></li>
        <ol>
            <li>Dodgeball</li>
            <li>Mini games</li>
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
    