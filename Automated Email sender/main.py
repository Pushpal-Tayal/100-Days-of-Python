#SMTP- Simple mail transfer protocol- Computer relies on this protocol for sending email.
#TLS- Transport layer security- for encryption of the mail content

import smtplib

my_email = "tayalpushpal@gmail.com"
password = "i6tqulz@99"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password= password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="tayalpushpal@gmail.com",
                        msg="Subject: Doing cool stuff \n\n Trying out automated mails with Python")
