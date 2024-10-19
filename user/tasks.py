from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserGuide
from django.core.mail import send_mail

# для получения данных запроса
from .middleware import get_current_request

from AccTrackGuides.celery import app


@app.task
def rate_send_mail(rated_user, rate):
    print('СИГНАЛ')
    subject = 'Your setup has been rated'
    message = f'Your setup has been {rate} by {rated_user}'
    recipient = 'nkorsakov230@gmail.com'
    send_from = 'nk041496@gmail.com'
    send_mail(subject, message, send_from, [recipient])