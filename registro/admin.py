from django.contrib import admin
from .models import registro
# Register your models here.

class registroAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')

admin.site.register(registro, registroAdmin)
