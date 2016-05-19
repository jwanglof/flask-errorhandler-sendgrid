#!/usr/bin/env python
# coding=utf-8
from distutils.core import setup
setup(
  name='flask-errorhandler-sendgrid',
  packages=['flask-errorhandler-sendgrid'],  # this must be the same as the name above
  version='0.1',
  description='A library that helps SendGrid-users to send emails to specified email-addresses when specified '
              'errors occurs',
  author='Johan Wänglöf',
  author_email='jwanglof@gmail.com',
  url='https://github.com/jwanglof/flask-errorhandler-sendgrid',  # use the URL to the github repo
  download_url='https://github.com/jwanglof/flask-errorhandler-sendgrid/tarball/0.1',  # I'll explain this in a second
  keywords=['sendgrid', 'errorhandling', 'error', 'flask'],  # arbitrary keywords
  classifiers=[],
)
