import smtplib
import json
import time
from verify_email import verify_email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, sender_name, sender_email, smtp_server, smtp_port, smtp_username, smtp_password):
        self.sender_name = sender_name
        self.sender_email = sender_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def send_email(self, receiver_email, subject, html_content):
        message = MIMEMultipart()
        message['From'] = f"{self.sender_name} <{self.sender_email}>"
        message['To'] = receiver_email
        message['Subject'] = subject

        html_part = MIMEText(html_content, 'html')
        message.attach(html_part)

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.sender_email, receiver_email, message.as_string())

        print("Email sent successfully!")

    def is_valid_email(self, email):
      return verify_email(email)

with open("mailmobs.json", 'r') as file:
  json_data = json.load(file)

email_sender = EmailSender(
    sender_name="Spliffpay",
    sender_email="hoods0014@yahoo.com",
    smtp_server="smtp.mail.yahoo.com",
    smtp_port=587,
    smtp_username="hoods0014@yahoo.com",
    smtp_password="rusxyosllojvkqbk"
)


html_content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Products | CryptoInvoice</title>
    <!-- Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
  </head>
  <body>
    <p style="display: none;">
      Streamline the invoicing process
      with a user-friendly interface.
      QR code generation for easy
      and accurate transfer.
    </p>
    <div marginheight="0" marginwidth="0" style="width:100%!important;margin:0;padding:0">
        <table style="border-collapse:collapse;padding:0;background-color:white;text-align:left;width:100%">
            <tbody style="border:none;padding:0;margin:0">
                <tr style="border:none;margin:0px;padding:0px">
                    <td colspan="3" style="border:none;padding:0;margin:0;text-align:center;">
                        <a href="https://www.spliffpay.biz/login">
                            <img src="https://www.techspliff.com/static/email_marketing_jpg.jpg" alt="..." style="display:block; margin:auto;">
                        </a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
  </body>    
</html>
"""

while True:
  try:
    email_list_empty = False
    for country_data in json_data:
        country, email_addresses = list(country_data.items())[0]       
        for email in email_addresses:
            if email_sender.is_valid_email(email):
                subject = "Crypto Invoice for your Business Needs"
                email_sender.send_email(email, subject, html_content)
                email_addresses.remove(email)
            else:
                print(f"{email} in {country} is not a valid email address.")
                email_addresses.remove(email)
     
        if len(email_addresses) == 0:
          print('email list is now empty')
          email_list_empty = True

        time.sleep(10)

    if email_list_empty:
      break
  
  except Exception as e:
    print(f"An error occurred: {e}")
    time.sleep(60)
