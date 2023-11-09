from django import forms
from .models import *
import datetime 


class StaffForm(forms.ModelForm):
    username = forms.CharField( max_length=30,required=True)
    profile =forms.ImageField( required=True)
    
    class Meta:
        model =User
    
        fields = ["username","first_name","last_name","password","email","gender","contact_number","dob","profile"]
        widgets = {'password':forms.HiddenInput(attrs={'class':'mypass'}),
                   "dob":forms.DateInput(attrs={'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.fields['password'].required = False

      
                            
class CustomerForm(forms.ModelForm):
       
    class Meta:
        model =User 
        fields = ("username","first_name","last_name","father_name","mother_name","gender","email","contact_number","dob","nationality","city","state",
                    "pincode","age","adhar_no","pan_no","address","marital_status","profile","password")
        widgets = {

                "dob":forms.DateInput(attrs={'type':'date'}),
                'username':forms.HiddenInput(attrs={'class':'username'}),
                'password':forms.PasswordInput(attrs={'mypass':'password'})

                # 'password':forms.HiddenInput(attrs={'class':'username'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        # self.fields['password'].required = False

    
       
        # #true

        self.fields['father_name'].required = True
        self.fields['mother_name'].required = True
        self.fields['gender'].required = True
        self.fields['city'].required = True
        self.fields['state'].required = True
        self.fields['pincode'].required = True
        self.fields['age'].required = True
        self.fields['adhar_no'].required = True
        self.fields['pan_no'].required = True
        self.fields['address'].required = True
        self.fields['marital_status'].required = True
        self.fields['profile'].required = True


class AccountForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ("accounts_type","account_no")
        widgets = {
                    'account_no':forms.HiddenInput(attrs={'class':'account_no'}),
                }

        def __init__(self, user, *args, **kwargs):

            self.fields['account_no'].required = False
  
class OpenAccountForm(forms.ModelForm):
    # accounts_type = forms.ModelChoiceField(queryset=Account.objects.all())

    class Meta:
        model = Account
        fields = ("accounts_type",)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        all_account_type_obj = Account.account_type
        existing_accounts = []
        
        for exist_account in self.user.user_account.filter(deleted= False):
            existing_accounts.append(exist_account.accounts_type) 
        
        all_account_type = []
        for account in all_account_type_obj:
            if account[0] not in existing_accounts:
                all_account_type.append(account[0])
        print(all_account_type)
        self.fields['accounts_type'].choices = [ choice for choice in all_account_type_obj if choice[0] in all_account_type ]
      
      