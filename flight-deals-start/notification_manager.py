
from twilio.rest import Client
from smtplib import SMTP

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER"

MY_EMAIL = 'animashaunjamal700@gmail.com'
MY_PASSWORD = 'eompqxrifixxvwpr'


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addr=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )