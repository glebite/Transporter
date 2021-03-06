"""
transporter - a specific type of emailer class
"""
#!/usr/bin/env python

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.
from smtplib import SMTP
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import logger

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
FH = logging.FileHandler('uatu.log')
FORMATTER = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')
FH.setFormatter(FORMATTER)
FH.setLevel(logging.DEBUG)
LOGGER.addHandler(FH)

class Transporter:
    """ Transporter """
    def __init__(self, from_address=None, to_address=None, user_password=None, subject=None):
        """ init function """
        self.msg_root = MIMEMultipart('related')
        self.msg_root['From'] = from_address
        self.msg_root['To'] = to_address
        self.msg_root['Subject'] = subject
        self.password = user_password
        self.string_message = ""
        self.msg_root.preamble = 'This is a multi-part message in MIME format.'
        self.msg_alternative = MIMEMultipart('alternative')
        self.msg_root.attach(self.msg_alternative)
        self.msg_text = MIMEText('This is the alternative plain text message.')
        self.msg_alternative.attach(self.msg_text)

    def build_message_text(self, string_message=""):
        """pi build_message_text """
        self.string_message += string_message

    def add_images(self, images=None):
        """ add_images """
        counter = 0
        string_message = "<br>{}<br>".format(self.string_message)
        if images:
            if isinstance(images, str):
                images = [images]
                LOGGER.info(f'images: {images}')
            for image_name in images:
                if os.path.exists(image_name):
                    string_message += '<img src=' \
                    '"cid:image{}"><br>{}<br>'.format(counter, image_name)
                    file_pointer = open(image_name, 'rb')
                    msg_image = MIMEImage(file_pointer.read(), _subtype="png")
                    file_pointer.close()
                    msg_image.add_header('Content-ID', '<image{}>'.format(counter))
                    self.msg_root.attach(msg_image)
                    counter += 1
                else:
                    LOGGER.info(f'File does not exist... {image_name}')
        self.msg_text = MIMEText(string_message, 'html')
        self.msg_alternative.attach(self.msg_text)

    def send_it(self):
        """ send it """
        smtp_server = SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        # smtp_server.ehlo
        if all(v is not None for v in [self.msg_root['From'], self.msg_root['To'], self.password]):
            smtp_server.login(self.msg_root['From'], self.password)
            smtp_server.sendmail(self.msg_root['From'],
                                 self.msg_root['To'],
                                 self.msg_root.as_string())
        else:
            raise ValueError
        smtp_server.close()


if __name__ == "__main__":
    FROM = sys.argv[1]
    TO = sys.argv[2]
    USER_PASSWORD = sys.argv[3]
    SUBJECT = sys.argv[4]
    IMAGES = sys.argv[5:]
    T_OBJ = Transporter(FROM, TO, USER_PASSWORD, 'Text stuff...')
    T_OBJ.build_message_text(string_message='Information...')
    T_OBJ.add_images(IMAGES)
    T_OBJ.send_it()
