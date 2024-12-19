import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_credentials():
    with open("secrets.json", "r") as file:
        credentials = json.load(file)
    return credentials["LOUIS_EMAIL"], credentials["VURAN_EMAIL"], credentials["LOUIS_PASSWORD"]
 
def send_email(best_move):
    subject = best_move
    body = "please relay the move in the subject line to our chess player"
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    sender_email, receiver_email, password = load_credentials()
    
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, password)
        s.sendmail(sender_email, sender_email, msg.as_string())
        # s.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        error_file_path = "errors.txt"
        with open(error_file_path, "a") as file:
            file.write(str(time.time) + ": " + str(e) + "\n")
    finally:
        s.quit()
 