from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(subject, email_content):

    sender = 'coremoringa@gmail.com'
    receiver = 'coremoringa@gmail.com'

    msg = EmailMultiAlternatives(subject, email_content, sender, [receiver])
    msg.attach_alternative(email_content, 'text/html')
    msg.send()
