from django.db import models
# from user.models import User
from guides.models import Car, Track
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserGuide(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name='user_guides')
    trackName = models.ForeignKey(to='guides.Track', on_delete=models.DO_NOTHING, related_name='guide_tracks')
    carName = models.ForeignKey(to='guides.Car', on_delete=models.DO_NOTHING, related_name='guide_cars')
    pass_time = models.CharField(max_length=64, blank=False, null=False, default='0')
    
    carSettings = models.JSONField()
    
class User(AbstractUser):
    username = models.CharField(max_length=128, unique=True)