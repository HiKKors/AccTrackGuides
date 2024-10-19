from django.contrib import admin
from .models import UserGuide, ViewCount, User, Review

# Register your models here.
admin.site.register(UserGuide)
admin.site.register(ViewCount)
admin.site.register(User)
admin.site.register(Review)
