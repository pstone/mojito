import requests
from api import app

class Mandrill:
    def __init__(self):
        self.api_url = app.config['MANDRILL_SEND_ENDPOINT']
        self.api_key = app.config['MANDRILL_API_KEY']

    def send(self):
        try:
            mandrill_client = mandrill.Mandrill('YOUR_API_KEY')
            message = {'attachments': [{'content': 'ZXhhbXBsZSBmaWxl',
                                        'name': 'myfile.txt',
                                        'type': 'text/plain'}],
                       'auto_html': None,
                       'auto_text': None,
                       'bcc_address': 'message.bcc_address@example.com',
                       'from_email': 'message.from_email@example.com',
                       'from_name': 'Example Name',
                       'global_merge_vars': [{'content': 'merge1 content', 'name': 'merge1'}],
                       'google_analytics_campaign': 'message.from_email@example.com',
                       'google_analytics_domains': ['example.com'],
                       'headers': {'Reply-To': 'message.reply@example.com'},
                       'html': '<p>Example HTML content</p>',
                       'images': [{'content': 'ZXhhbXBsZSBmaWxl',
                                   'name': 'IMAGECID',
                                   'type': 'image/png'}],
                       'important': False,
                       'inline_css': None,
                       'merge': True,
                       'merge_language': 'mailchimp',
                       'merge_vars': [{'rcpt': 'recipient.email@example.com',
                                       'vars': [{'content': 'merge2 content', 'name': 'merge2'}]}],
                       'metadata': {'website': 'www.example.com'},
                       'preserve_recipients': None,
                       'recipient_metadata': [{'rcpt': 'recipient.email@example.com',
                                               'values': {'user_id': 123456}}],
                       'return_path_domain': None,
                       'signing_domain': None,
                       'subaccount': 'customer-123',
                       'subject': 'example subject',
                       'tags': ['password-resets'],
                       'text': 'Example text content',
                       'to': [{'email': 'recipient.email@example.com',
                               'name': 'Recipient Name',
                               'type': 'to'}],
                       'track_clicks': None,
                       'track_opens': None,
                       'tracking_domain': None,
                       'url_strip_qs': None,
                       'view_content_link': None}
            result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool',
                                                   send_at='example send_at')
            '''
            [{'_id': 'abc123abc123abc123abc123abc123',
              'email': 'recipient.email@example.com',
              'reject_reason': 'hard-bounce',
              'status': 'sent'}]
            '''

        except mandrill.Error, e:
            # Mandrill errors are thrown as exceptions
            print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
            # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'
            raise