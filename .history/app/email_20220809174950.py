from flask import current_app, render_template
from flask_mail import Message
from app import mail

def send_reset_password_mail(user, token):
    msg = Message("Reset Your Password",
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[user.email],
                  html=render_template('reset_password_mail.html', token=token))