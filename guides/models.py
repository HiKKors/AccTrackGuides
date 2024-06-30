from django.db import models

# Create your models here.
class GuideData(models.Model):
    id = models.AutoField(primary_key=True)
    trackName = models.ForeignKey(to='Track', on_delete=models.DO_NOTHING)
    carName = models.ForeignKey(to='Car', on_delete=models.DO_NOTHING)
    time = models.CharField(max_length=64, null=False, blank=False)
    video_url = models.CharField(max_length=500, null=False, blank=False)
    
    carSettings = models.JSONField()
    
    def __str__(self):
        return f'{self.trackName}, {self.carName}'
    

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    image = models.ImageField(upload_to='cars_imgs', blank=True)
    
    def __str__(self):
        return f'{self.name}'
    

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    image = models.ImageField(upload_to='tracks_imgs', blank=True)
    
    def __str__(self):
        return self.name