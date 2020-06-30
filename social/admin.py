from django.contrib import admin
from social.models import Platforms
# Register your models here.

admin.register(Platforms)

class PlatformsAdmin(admin.ModelAdmin):
    list_display = ('s_name','p_email','p_password',)
    