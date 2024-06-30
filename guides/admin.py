from django.contrib import admin

from .models import GuideData, Car, Track

# Register your models here.
admin.site.register(GuideData)
admin.site.register(Car)
admin.site.register(Track)
