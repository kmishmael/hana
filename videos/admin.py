from django.contrib import admin
from videos.models import Video
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_id','name','videourl')

admin.site.register(Video, VideoAdmin)
