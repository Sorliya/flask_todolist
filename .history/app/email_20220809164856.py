from flask import current_app, render_template
from flask_mail import Message
from app import mail

def send_reset_password_mail(user, token):
    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=["to@example.com"])