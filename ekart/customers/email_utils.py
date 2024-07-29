from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(user_email):
    subject = 'Welcome to Our E-commerce Site'
    message = 'Thank you for registering on our site.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)