import os

from celery import Celery

# Установка модуля настроек Django по умолчанию для программы "celery".
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AccTrackGuides.settings')

app = Celery('AccTrackGuides', broker='redis://localhost:6379')

# Использование строки здесь означает, что работнику не нужно сериализовать объект конфигурации для дочерних процессов. 
# - namespace='CELERY' означает, что все клавиши конфигурации, 
# связанные с сельдереем, должны иметь префикс `CELERY_`.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузка модулей задач из всех зарегистрированных приложений Django.
app.autodiscover_tasks()