from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import os

load_dotenv()

EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD=os.getenv("EMAIL_PASSWORD")

if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise RuntimeError("Email credentials not set in environmental variables")

def send_otp_to_email(email_id:str,otp:str):
    msg=EmailMessage()
    msg["subject"]="your veification OTP"
    msg["From"]=EMAIL_ADDRESS
    msg["To"]=email_id
    msg.set_content(f"your verification is:{otp}")
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)

    except Exception as e:
        raise RuntimeError(f"Failed to send Otp To email:{str(e)}")
    
    


