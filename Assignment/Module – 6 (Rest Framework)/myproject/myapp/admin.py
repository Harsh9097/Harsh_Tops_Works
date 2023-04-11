from django.contrib import admin
from .models import *

# Register your models here.
class AdminBook(admin.ModelAdmin):
    list_display = ("title","author","isbn","publisher")
admin.site.register(Book,AdminBook)
