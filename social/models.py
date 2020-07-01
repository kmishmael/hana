from django.db import models
from django.urls import reverse

# Create your models here.
PLATFORMS = (
    ("Spotify","Spotify"),
    ("Facebook","Facebook"),
    ("Twitter","Twitter"),
    ("Github","Github"),
    ("Google","Google"),
    ("Instagram","Instagram"),
    ("Microsoft","Microsoft"),
    ("Wordpress","Wordpress"),
    ("Youtube","Youtube"),
    ("Whatsapp","Whatsapp"),
)

class Platforms(models.Model):
    id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=30,verbose_name='Platform',choices=PLATFORMS)
    p_username = models.CharField(max_length=30,verbose_name='Username')
    p_email = models.EmailField(max_length=30,verbose_name='Email')
    p_name = models.CharField(max_length=30,verbose_name='Name')
    p_password = models.CharField(max_length=30,verbose_name='Password')
    f_class = models.CharField(max_length=30,verbose_name='Icon')
    
    def __str__(self):
        return self.s_name
    
    def get_absolute_url(self):
        return reverse('platform-detail', args=[str(self.id)])
        
