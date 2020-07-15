from django.db import models

# Create your models here.

class Journal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Name')
    date = models.DateField(verbose_name='Date')
    journalurl = models.URLField(max_length=200, verbose_name='Url', blank=True)
    journal = models.TextField(verbose_name='Journal',blank=True)
    journaldoc = models.FileField(upload_to='Thumbnails/journals/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    