#!/usr/bin/env python

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# # Define these once; use them twice!
# strFrom = sys.argv[2]
# strTo = sys.argv[3]
# password = sys.argv[4]

# # Create the root message and fill in the from, to, and subject headers
# msgRoot = MIMEMultipart('related')
# msgRoot['Subject'] = sys.argv[1]
# msgRoot['From'] = strFrom
# sender = strFrom
# msgRoot['To'] = strTo
# receiver = strTo
# msgRoot.preamble = 'This is a multi-part message in MIME format.'

# # Encapsulate the plain and HTML versions of the message body in an
# # 'alternative' part, so message agents can decide which they want to display.
# msgAlternative = MIMEMultipart('alternative')
# msgRoot.attach(msgAlternative)

# msgText = MIMEText('This is the alternative plain text message.')
# msgAlternative.attach(msgText)

# string_message = 'Security images.'
# counter = 0
# for image_name in sys.argv[5:]:
#     print('Working on image: ' + image_name)
#     # We reference the image in the IMG SRC attribute by the ID we give it below
#     string_message += '<img src="cid:image{}"><br>'.format(counter)
#     fp = open(image_name,'rb')
#     msgImage = MIMEImage(fp.read(), _subtype="jpg")
#     fp.close()
#     msgImage.add_header('Content-ID', '<image{}>'.format(counter))
#     msgRoot.attach(msgImage)
#     counter += 1

# msgText = MIMEText(string_message, 'html')
# msgAlternative.attach(msgText)

# smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
# smtpserver.ehlo()
# smtpserver.starttls()
# smtpserver.ehlo
# smtpserver.login(sender, password)
# smtpserver.sendmail(sender, receiver, msgRoot.as_string())
# smtpserver.close()

class Transporter:
    """ Transporter """
    def __init__(self):
        """ init function """

    def build_message_text(self):
        """ build_message_text """

    def add_images(self):
        """ add_images """

    def send_it(self):
        """ send it """
        
