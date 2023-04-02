import smtplib, ssl
import os

class Email:
    def send(this, message):
        host = "smtp.gmail.com"
        port = 465

        username = "itmandjango@gmail.com"
        password = os.getenv("portfolio_password")

        receiver = "itmanco@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)

        print("email sended...")