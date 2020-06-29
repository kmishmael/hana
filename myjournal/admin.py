from django.contrib import admin

from myjournal.models import Name

# Register your models here.

#class JournalAdmin(admin.ModelAdmin):
 #   list_display = ('j_date','j_time','j_title',)
admin.register(Name)

class NameAdmin(admin.ModelAdmin):
    list_display = ('type','email','password',)

admin.site.register(Name, NameAdmin)
