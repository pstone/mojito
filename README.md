# Project Mojito

A HTTP emailing service that delivers email via Mailgun or Mandrill

## Built With

* [Flask](http://flask.pocoo.org) - A Python micro framework 


## Getting Started

```
git clone https://github.com/pstone/mojito
```

### Prerequisites

Python 2.6 or newer

```
$ python -V
Python 2.7.13
```

### Installing

Set up virtual env

```
cd mojito
sudo pip install virtualenv
virtualenv venv
. venv/bin/activate
```

then install packages
```
pip install -r requirements.txt
```

Finally run
```
export FLASK_APP=./api/routes.py
flask run
```
### Email Provider
Mailgun and Mnadrill are used for outbound mail.  

To switch provider, change the config in api/__init__.py
```
app.config['MAIL_PROVIDER'] = 'MAILGUN'
```
```
app.config['MAIL_PROVIDER'] = 'MANDRILL'
```
### API Endpoints
POST /email

Sample request:
```
curl -H "Content-Type: application/json" -X POST -d '{"to":"pamelastone@gmail.com","to_name":"Pam Lu","from":"pamela.stone@gmail.com", "from_name": "Pam Sender", "subject": "A Message", "body": "<h1>Your Bill</h1><p>$10</p>"}' http://127.0.0.1:5000/email
```

### Testing

```
python test.py
```

## Deployment
Configuration files are set up for CircleCI and Heroku.  

* [CircleCI](http://circleci.com) - Deployment tool
* [Heroku](http://heroku.com) - Application Hosting

You need to update app name in circle.yml to your Heroku host name.
```
heroku:
      appname: peaceful-gorge-35511
```

### To do
- Create env specific configs for dev, stage and production
- Use system config to store API keys securely
- Better error handling and messages

### Production ready
- Use queue for incoming messages 
- API should allow 1+ outbound emails for bulk mailing
- Set up third-party API monitoring to ensure service is up
- Set up application monitoring (e.g. sentry, new relic) to track errors
- Set up system monitoring