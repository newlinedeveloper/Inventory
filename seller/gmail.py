#sending email

import smtplib
def gmail(password):
    s = smtplib.SMTP('smtp.gmail.com',587)

    s.starttls()

    s.login("veerasolaiyappan@gmail.com","Veeresh26011999")

    message = password

    if s.sendmail("veerasolaiyappan@gmail.com","newlinedeveloper@gmail.com",message) is True:
        print("message sent successfully!!!")

    s.quit()



'''
#simple mail
import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'USERNAME or EMAIL ADDRESS'
password = 'PASSWORD'
sender = 'ME@EXAMPLE.COM'
targets = ['HE@EXAMPLE.COM', 'SHE@EXAMPLE.COM']

msg = MIMEText('Hi, how are you today?')
msg['Subject'] = 'Hello'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()


#attachment]

'''
