from flask import Flask
from flask_restful import Api
import logging

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['BUNDLE_ERRORS'] = True

app.config['MAIL_PROVIDER'] = 'MAILGUN'

app.config['MAILGUN_API_SEND'] = 'https://api.mailgun.net/v3/sandbox94f6ab5904f544dba32852a3e3d4cf1c.mailgun.org/messages'
app.config['MAILGUN_API_KEY'] = 'key-066b9601c57c65b9c272a18110486770'

app.config['MANDRILL_API_SEND'] = 'https://mandrillapp.com/api/1.0/messages/send.json'
#this is a test key, no email will be sent
app.config['MANDRILL_API_KEY'] = 'pcjAk56VhMGrpqz5qWHGLg'


restApi = Api(app)

import api.routes, model