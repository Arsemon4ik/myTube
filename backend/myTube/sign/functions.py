from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from decouple import config
from twilio.rest import Client


def send_congratulations_by_mail(email, username):
    html_content = render_to_string(
        'sign/mail/send_congr.html',
        {
            'username': username,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Добро пожаловать!',
        from_email='arseniy.reima@gmail.com',
        to=[email],  # это то же, что и recipients_list
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html

    msg.send()  # отсылаем


def send_congratulations_by_phone(phone, username):
    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"{username}! Добро пожаловать на сайт myTube!",
        from_='+19124937868',
        to=f'{phone}'
    )
