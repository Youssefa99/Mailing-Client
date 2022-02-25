import smtplib
import ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Create a secure SSL context
context = ssl.create_default_context()

# Address of email service provider
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
# start service
    server.ehlo()
except:
    print('Connection error')

# ideally password should be read from an external file for security purposes
server.login('youremail@gmail.com', 'yourpassword')

# define email structure From, to, subject and body


msg = MIMEMultipart()
msg['From'] = 'youssef'
msg['To'] = '7amo'
msg['Subject'] = 'Test mail Client'
message = 'Mail Client Works'
msg.attach(MIMEText(message, 'plain'))
filename = 'TestImage.png'
attachment = open(filename, 'rb')


# indicates that payload is a binary file
payload = MIMEBase('application', 'octet-stream')
payload.set_payload(attachment.read())


# encode using base 64 as data is non-text
encoders.encode_base64(payload)


# indicates content is an attachment in this case as the image is treated as an attachment
payload.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(payload)

email = msg.as_string()
server.sendmail('senderemail@gmail.com', 'receiveremail@gmail.com', email)
