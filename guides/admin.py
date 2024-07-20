from django.contrib import admin

from .models import GuideData, Car, Track, CarFrontLook

# Register your models here.
admin.site.register(GuideData)
admin.site.register(Car)
admin.site.register(Track)
admin.site.register(CarFrontLook)


admin.AdminSite.site_url = '/news'
