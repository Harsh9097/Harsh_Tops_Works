from django.contrib import admin
from .models import *

# Register your models here.

class AdminNotice(admin.ModelAdmin):
    list_display = ("title","description")

class AdminEvent(admin.ModelAdmin):
    list_display = ("title","description")

admin.site.register(Notice,AdminNotice)
admin.site.register(Event,AdminEvent)