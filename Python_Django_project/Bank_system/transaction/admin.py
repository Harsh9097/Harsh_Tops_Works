from django.contrib import admin
from .models import *
# # # Register your models here.
admin.site.register(Transaction)
# @admin.register(Deposit)
# class DepositAdmin(admin.ModelAdmin):
#     list_display = ("depositor_name","account_no","amount", "deposit_date","is_approve")

# @admin.register(Withdraw)
# class WithdrawAdmin(admin.ModelAdmin):
#     list_display = ("account_holder_name","account_no","amount")

# @admin.register(Transaction)
# class TransactionAdmin(admin.ModelAdmin):
#     list_display = ("transaction_type_choice","withdrawn","deposited")


# admin.site.register(Transfer)


# @admin.register(ATM)
# class ATMAdmin(admin.ModelAdmin):
#     list_display = ("name","account_no","address", "account_no","is_approve")