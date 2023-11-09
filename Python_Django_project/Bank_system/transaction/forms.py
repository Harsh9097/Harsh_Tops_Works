from typing import Any, Dict
from django import forms
from .models import *
from django.core import validators
from django.contrib import messages
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect





class DepositForm(forms.ModelForm):
    account_no = forms.CharField(required=True)
    contact_number =forms.CharField( max_length=10, required=True)

    class Meta:
        model = Transaction 

        fields = ("depositor_name","account_no","amount","contact_number")
        widgets = {
                    
                 }

    def clean_account_no(self):
        account_no = self.cleaned_data.get("account_no")

        if not Account.objects.filter(account_no=account_no).exists():
            raise forms.ValidationError("Provided account number is invalid. ")

        return account_no
    
    def save(self, commit=True):
        account_no = self.cleaned_data['account_no']
        transaction_obj = super().save(commit=False)
        transaction_obj.transactions_type = Transaction.CREDIT
        transaction_obj.is_approve=False

        if Account.objects.filter(account_no=account_no).exists():
            account_obj = Account.objects.get(account_no=account_no)
            transaction_obj.account = account_obj
            transaction_obj.save(commit)
            return transaction_obj
      

class WithdrawForm(forms.ModelForm):
    account_no =forms.CharField(max_length=12, required=True)
    security_pin = forms.IntegerField(required=True,widget=forms.PasswordInput())
    class Meta:
        model=Transaction
        fields = ('account_holder_name','account_no','amount','security_pin')

    
    def clean_account_no(self):
        account_no = self.cleaned_data.get("account_no")

        if not Account.objects.filter(account_no=account_no).exists():
            raise forms.ValidationError("Provided account number is invalid. ")

        return account_no

    def clean_security_pin(self):
        security_pin = self.cleaned_data.get("security_pin")
        account_no  = self.cleaned_data.get("account_no")

        account = Account.objects.get(account_no=account_no)

        if account.security_pin != security_pin:
            raise forms.ValidationError("Provided security pin is invalid.")

        return security_pin

    
    def clean_amount(self):
        amount = self.cleaned_data.get("amount")
        account_no=self.cleaned_data.get("account_no")


        account = Account.objects.get(account_no=account_no)

        if account.balance < amount:
            raise forms.ValidationError("Insufficient balance.")
        return amount

class CreatePinForm(forms.ModelForm): 
    confirm_security_pin = forms.IntegerField(required=True,widget=forms.PasswordInput())

    class Meta:
        model =Account
        fields = ("accounts_type","account_no","security_pin" ,"confirm_security_pin")
        
        widgets = {

                   'security_pin':forms.PasswordInput(attrs={'type':'password'})
                    
                 }
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        existing_accounts = [account.accounts_type for account in self.user.user_account.filter(deleted=False)]
        all_account_type_obj = Account.account_type

        self.fields['accounts_type'].choices = [(choice, label) for choice, label in all_account_type_obj if choice in existing_accounts]

        first_selected_account_type = user.user_account.first().accounts_type

        initial_account = Account.objects.filter(user=user, accounts_type=first_selected_account_type).first()

        if initial_account:
            self.fields['account_no'].initial = initial_account.account_no
            self.fields['account_no'].widget.attrs['readonly'] = True
        
    def clean_confirm_security_pin(self):

        security_pin = self.cleaned_data['security_pin']
        confirm_security_pin = self.cleaned_data['confirm_security_pin']
      

        if security_pin != confirm_security_pin:
            raise forms.ValidationError("security pin is not match. ")
        return confirm_security_pin
         


class TransferForm(forms.ModelForm):
    accounts_type = forms.ChoiceField(choices=Account.account_type, required=True)
    from_account_number = forms.CharField(max_length=13,required=True)
    security_pin = forms.IntegerField(required=True, widget=forms.PasswordInput())
    
    class Meta:
        model = Transaction
        fields = ("accounts_type","from_account_number","to_account_number","amount","security_pin")

                 
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        self.from_account = None
        super().__init__(*args, **kwargs)

        existing_accounts = [account.accounts_type for account in self.user.user_account.filter(deleted=False)]
        all_account_type_obj = Account.account_type

        self.fields['accounts_type'].choices = [(choice, label) for choice, label in all_account_type_obj if choice in existing_accounts]

        #fist value default
        first_selected_account_type = self.user.user_account.first().accounts_type

        initial_account = Account.objects.filter(user=self.user, accounts_type=first_selected_account_type).first()

        if initial_account:
            self.fields['from_account_number'].initial = initial_account.account_no
            self.fields['from_account_number'].widget.attrs['readonly'] = True
            self.fields['to_account_number'].required = True


    def clean_from_account_number(self):
        from_account_number = self.cleaned_data.get("from_account_number")
        try:
            self.from_account = Account.objects.get(account_no=from_account_number, user=self.user)
        except Exception:
            raise forms.ValidationError("Provided account number is invalid. ")

        return self.from_account

    def clean_to_account_number(self):
        from_account_number = self.cleaned_data.get("from_account_number")
        to_account_number = self.cleaned_data.get("to_account_number")

        if  from_account_number.account_no == to_account_number:
            raise forms.ValidationError("Recipient account number should be different than from account.")

        try:
            self.to_account = Account.objects.get(account_no=to_account_number)
        except Exception:
                raise forms.ValidationError("Provided account number is invalid. ")
        
        
        return self.to_account

    def clean_security_pin(self):
        security_pin = self.cleaned_data.get("security_pin")

        if self.from_account.security_pin != security_pin:
            raise forms.ValidationError("Provided security pin is invalid.")

        return security_pin


    def clean_amount(self):
        amount = self.cleaned_data.get("amount")

        if self.from_account.balance < amount:
            raise forms.ValidationError("Insufficient balance.")
        return amount
 