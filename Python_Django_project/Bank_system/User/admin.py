from django.contrib import admin
from .models import *
# # Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("role","first_name","last_name","gender")

# class AccountAdmin(admin.ModelAdmin):
#     list_display = ("user","accounts_Type","account_no","security_pin")
admin.site.register(Account)