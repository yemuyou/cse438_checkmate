import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# create email subject and body you want to send
subject = "Test Subject"
body = "test body"
msg = MIMEMultipart()
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# sign into gmail and send message
sender_email = "sender email"
sender_password = "sender password"
receiver_email = "receiver email"

s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email, sender_password)
# message to be sent
message = "test message"
# sending the mail
s.sendmail(sender_email, receiver_email, msg.as_string())
# terminating the session
s.quit()



