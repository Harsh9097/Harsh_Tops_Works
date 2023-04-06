from django.contrib import admin
from .models import *

# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ("id","name","email","city")
    list_display_links =('name',)
    list_filter=('city',)
    list_editable = ('city',)
    search_fields = ('name',)
    list_per_page = 5
admin.site.register(Studnet,AdminStudent)