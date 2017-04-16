from api import app
from jsonschema import validate
from api.schema import emailSchema
from html2text import html2text
from validate_email import validate_email
from mailgun import Mailgun
from mandrill import Mandrill

class Email(object):
    def __init__(self, args):
        try:
            validate(args, emailSchema)

            if validate_email(args['to']) and validate_email(args['from']):
                self.to_email = args['to']
                self.to_name = args['to_name']
                self.from_email = args['from']
                self.from_name = args['from_name']
                self.subject = args['subject']
                self.body = html2text(args['body'])
                self.is_valid = True
            else:
                self.is_valid = False
        except:
            self.is_valid = False



    def send(self):
        if app.config['TESTING'] != True:
            if app.config['MAIL_PROVIDER'] == 'MAILGUN':
                emailProvider = Mailgun(app.config['MAILGUN_API_SEND'], app.config['MAILGUN_API_KEY'])

            elif app.config['MAIL_PROVIDER'] == 'MANDRILL':
                emailProvider = Mandrill(app.config['MANDRILL_API_SEND'], app.config['MANDRILL_API_KEY'])

            emailProvider.send_message(self)
