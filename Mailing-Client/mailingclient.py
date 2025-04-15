import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 25)
server.connect("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.ehlo
server.login("biel@gmail.com", "psswrd")

msg = MIMEMultipart()
msg["From"] = "Biel"
msg["To"] = "test@gmail.com"
msg["Subject"] = "Test"


message="Hola!"
msg.attach(MIMEText(message), "plain")

text = msg.as_string()
server.sendmail("biel@gmail.com","t@gmail.com", text)




server.quit()
