from django.contrib import admin
from documents.models import Document
# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_id','name','documenturl')

admin.site.register(Document, DocumentAdmin)
