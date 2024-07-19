from .models import ViewCount
from .utils import get_user_ip

class ViewCountMixin:
    def get_object(self):
        # получаем статью из метода родительского класса
        obj = super().get_object()
        # получаем IP-адрес пользователя
        ip_address = get_user_ip(self.request)
        # получаем или создаем запись о просмотре статьи для данного пользователя
        ViewCount.objects.get_or_create(setup=obj, ip_adress=ip_address)
        return obj