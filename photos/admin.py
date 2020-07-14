from django.contrib import admin
from photos.models import Image
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_id','name','imageurl')

admin.site.register(Image, ImageAdmin)
