from django.contrib import admin
from social.models import Name
# Register your models here.

admin.register(Name)

class NameAdmin(admin.ModelAdmin):
    list_display = ('type','email','password',)

admin.site.register(Name, NameAdmin)
