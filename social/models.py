from django.db import models
# Create your models here.
PLATFORMS = (
    ("s","Spotify"),
    ("f","Facebook"),
    ("t","twitter"),
    ("i","Github"),
    ("g","Google"),
    ("ig","instagram"),
    ("w","windows"),
    ("o","worpress"),
    ("y","youtube"),
    ("w","whatsapp"),
)
class Name(models.Model):
    type = models.CharField(verbose_name='Platform', choices=PLATFORMS,max_length=30)
    email = models.EmailField(verbose_name='Email', max_length=50, default='kmishmael@gmail.com')
    name = models.CharField(verbose_name='Name', max_length=50, default=None)
    username = models.CharField(verbose_name='Username',max_length=30)
    password = models.CharField(max_length=30, verbose_name='Password')
    
    def __str__(self):
        return self.type