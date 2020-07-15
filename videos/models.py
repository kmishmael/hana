from django.db import models

# Create your models here.
class Video(models.Model):
    video_id = models.CharField(max_length=50, verbose_name='Id')
    name = models.CharField(max_length=100, verbose_name='Name')
    type = models.CharField(max_length=30, verbose_name='Mimetype')
    videourl = models.URLField(max_length=200, verbose_name='Url')
    video = models.FileField(upload_to='Videos/', blank=True, null=True)
    thumbnail = models.FileField(upload_to='Thumbnails/videos/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    