"""
transporter - a specific type of emailer class
"""
#!/usr/bin/env python

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

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

class Transporter:
    """ Transporter """
    def __init__(self, from_address=None, to_address=None, user_password=None):
        """ init function """
        self.sender = from_address
        self.receiver = to_address
        self.password = user_password
        self.string_message = ""        
        self.msg_text = MIMEMultipart('related')

    def build_message_text(self, subject_text=None,
                           preamble_text=None,
                           string_message=None):
        """ build_message_text """
        self.string_message += string_message

    def add_images(self, images=None):
        """ add_images """
        counter = 0
        for image_name in images:
            self.string_message += '<img src="cid:image{}"><br>'.format(counter)
            file_pointer = open(image_name, 'rb')
            msg_image = MIMEImage(file_pointer.read(), _subtype="jpg")
            file_pointer.close
            msg_image.add_header('Content-ID', '<image{}>'.format(counter))
            self.msg_text.attach(msg_image)
            counter += 1

    def send_it(self):
        """ send it """
        smtp_server = smptlib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smpt_server.login(self.sender, self.password)
        smpt_server.sendmail(self.sender,
                             self.receiver,
                             self.msg_text.as_string())
        smtp_server.close()
