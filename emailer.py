import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
#gmail app specific password: npro bbbe ffrh vnmx
#modified for my gmail
def send_email(best_move):
    subject = best_move
    body = "please relay the move in the subject line to our chess player"
    msg = MIMEMultipart()
    # msg['From'] = sender_email
    # msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("louantinoro@gmail.com", "npro bbbe ffrh vnmx")
    # message to be sent
    message = "test message"
    # sending the mail
    s.sendmail("louantinoro@gmail.com", "louantinoro@gmail.com", msg.as_string())
    # s.sendmail("louantinoro@gmail.com", "mcv@unl.edu", msg.as_string())
    # terminating the session
    s.quit()
 
