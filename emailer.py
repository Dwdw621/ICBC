import smtplib
import ssl
from email.message import EmailMessage

def emailer():
    try:
        sender = "washucoursenotifier@gmail.com"
        password = "qihcljmewlapdpyx"
        receiver = ["dylanwang2004@gmail.com"]

        subject = f"ICBC ROAD TEST OPEN!!"
        body = f"""
        https://onlinebusiness.icbc.com/webdeas-ui/booking
        """

        em = EmailMessage()
        em["From"] = sender
        em["To"] = receiver
        em["Subject"] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, em.as_string())
        print("Email sent!")
    except:
        print("Email error!")
