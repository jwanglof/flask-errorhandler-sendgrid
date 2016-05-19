# flask-errorhandler-sendgrid
A small library that makes it easier for SendGrid-users to be able to get e-mails when something errors on their Flask application. I created this because I couldn't find a similar error handler-library for Flask with SendGrid, and it's also my first PyPi-package so that's always something.

This package is inspired from [Flask-ErrorMail](https://github.com/jasonwyatt/Flask-ErrorMail). This package will focus on a more general approach and also integrate with [SendGrid](https://sendgrid.com/) instead of having our own SMTP-server.