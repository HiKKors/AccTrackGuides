from django.contrib import admin
from .models import UserGuide, ViewCount

# Register your models here.
admin.site.register(UserGuide)
admin.site.register(ViewCount)