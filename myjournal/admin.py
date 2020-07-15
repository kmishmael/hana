from django.contrib import admin
from myjournal.models import Journal
# Register your models here.
class JournalAdmin(admin.ModelAdmin):
    list_display = ('date','name','journalurl')

admin.site.register(Journal, JournalAdmin)
