from django.db import models
from django.core.files import File
from PIL import Image as img
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile, SimpleUploadedFile
from resizeimage import resizeimage
import urllib.request
from urllib.parse import urlparse, parse_qs

# Create your models here.

def compress(image):
    im = img.open(image)
    #im = resizeimage.resize('thumbnail', i, [250, 250])
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=60) 
    new_image = File(im_io, name=image.name)
    return new_image

def generate_thumbnail(image):
    t = img.open(image)
    thumbnail = resizeimage.resize('thumbnail', t, [250, 250])
    t_io = BytesIO()
    thumbnail.save(t_io, 'JPEG', quality=60)
    new_thumbnail = File(t_io, name=image.name)
    return new_thumbnail

def stream_url(stream_url):
    basename = urlparse(stream_url)
    #.path.split('/')[-1]dsd
    try:
        f_basename = parse_qs(basename.query)['id'][0] + ".jpeg"
    except KeyError:
        f_basename = basename.path.split('/')[-1]
    tmpfile,_ = urllib.request.urlretrieve(stream_url, "image.jpeg") 
    new_stream = SimpleUploadedFile(f_basename, open(tmpfile, "rb").read())
    return new_stream
class Image(models.Model):
    image_id = models.CharField(max_length=50, verbose_name='Id')
    name = models.CharField(max_length=100, verbose_name='Name')
    type = models.CharField(max_length=30, verbose_name='Mimetype')
    imageurl = models.URLField(max_length=200, verbose_name='Url')
    image = models.ImageField(upload_to='Images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='Thumbnails/photos/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        new_stream = stream_url(self.imageurl)
        self.image = new_stream
        new_image = compress(self.image)
        self.image = new_image
        new_thumbnail = generate_thumbnail(self.image)
        self.thumbnail = new_thumbnail
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    