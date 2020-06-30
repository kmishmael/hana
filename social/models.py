from django.db import models
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
    ("Yputube","Youtube"),
    ("Whatsapp","Whatsapp"),
)
class Platforms(models.Model):
    s_name = models.CharField(max_length=30,verbose_name='Platform',choices=PLATFORMS)
    p_username = models.CharField(max_length=30,verbose_name='Username')
    p_email = models.EmailField(max_length=30,verbose_name='Email')
    p_name = models.CharField(max_length=30,verbose_name='Name')
    p_password = models.CharField(max_length=30,verbose_name='Password')
    f_class = models.CharField(max_length=30,verbose_name='Icon')
    
    def __str__(self):
        return self.s_name
    