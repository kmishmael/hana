from django.db import models

# Create your models here.
class Document(models.Model):
    document_id = models.CharField(max_length=50, verbose_name='Id')
    name = models.CharField(max_length=100, verbose_name='Name')
    type = models.CharField(max_length=30, verbose_name='Mimetype')
    documenturl = models.URLField(max_length=200, verbose_name='Url')
    document = models.FileField(upload_to='Documents/', blank=True, null=True)
    document = models.FileField(upload_to='Thumbnails/documents/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    