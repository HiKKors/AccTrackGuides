from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserGuide
from django.core.mail import send_mail

# для получения данных запроса
from .middleware import get_current_request

from AccTrackGuides.celery import app

# @receiver(post_save, sender=UserGuide)
# @receiver(post_delete, sender=UserGuide)
# def invalidate_cache(sender, instance, **kwargs):
#     cache_key = 'views.decorators.cache.cache_page.AllCommunitySetups.get'
#     cache.delete(cache_key)
    
@app.task() 
@receiver(post_save, sender=UserGuide) #нужный запрос    таблица бд в которой происходит сохранение
def rate_send_mail(sender, instance, **kwargs):
    request = get_current_request()
    
    rate_up = request.POST.get('like')
    rate_down = request.POST.get('dislike')
    
    rate = ''
    if rate_up == '':
        rate = 'liked'
    elif rate_down == '':
        rate = 'disliked'
    
    subject = 'Your setup has been rated' # тема сообщения
    rated_by = request.user
    message = f'Your setup has been {rate} by {rated_by}' # само сообщение
    recipient = 'nkorsakov230@gmail.com' # получатель
    send_from = 'nk041496@gmai.com' # отправитель
    send_mail(subject, message, send_from, [recipient])
    
    # print('rated by:', request)
    
    # print("SENDER", sender)
    # print("INSTANCE", instance)
    # print("KWARGS", kwargs)
    
    