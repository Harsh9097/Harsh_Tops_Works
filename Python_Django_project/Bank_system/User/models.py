from django.db import models
from base.mymodels import BaseModel
from django.contrib.auth.models import AbstractUser
#Create your models here.


class User(AbstractUser, BaseModel):
    Male = "Male"
    FEMALE = "Female"
    OTHER = "Other"

    gender_type = (
        ('Male',Male),
        ('Female',FEMALE),
        ('Other',OTHER)
    )

    MANAGER ="Manager"
    STAFF ="Staff"
    CUSTOMER ="Customer"

    user_type = (
        ('Manager',MANAGER),
        ('Staff',STAFF),
        ('Customer',CUSTOMER)
    )

    MARRIED ="Married"
    UNMARRIED ="Unmarried"
    marital_type =(
             ('Married',MARRIED),
            ('Unmarried',UNMARRIED)
     )  



    role = models.CharField(max_length=20,choices=user_type,null=True,blank=True)
    contact_number  = models.BigIntegerField(null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    gender =models.CharField(max_length=30,choices=gender_type,default='0')
    adhar_no = models.BigIntegerField(null=True,blank=True) 
    pan_no = models.CharField(max_length=10,null=True,blank=True)      
    address = models.TextField(max_length=50,null=True,blank=True)    
    profile = models.ImageField(upload_to= "profile/", height_field=None, width_field=None, max_length=None,null=True,blank=True)
    father_name = models.CharField(max_length=50,null=True,blank=True)
    mother_name = models.CharField(max_length=50,null=True,blank=True)
    nationality = models.CharField(max_length=50,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    marital_status = models.CharField(choices=marital_type,max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.first_name
    


class Account(BaseModel):

    SAVING_ACCOUNT= "Saving Account"
    CURRENT_ACCOUNT= "Current Account"
    PERSONAL_ACCOUNT = "Personal Account"
    RECURRING_DEPOSIT = "Recurring Deposit"
    FIXED_DEPOSIT_ACCOUNT = "Fixed Deposit Account"
    account_type=(
            ('Saving Account' , SAVING_ACCOUNT),
            ('Current Account' , CURRENT_ACCOUNT ),
            ('Personal Account' , PERSONAL_ACCOUNT ),
            ('Recurring Deposit', RECURRING_DEPOSIT),
            ('Fixed Deposit Account' ,FIXED_DEPOSIT_ACCOUNT  )
    )  
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_account")
    accounts_type =  models.CharField(max_length=30,choices=account_type)
    account_no = models.CharField(max_length=50)
    
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0 ,null=True, blank=True)
    security_pin =models.IntegerField(default=None, null=True, blank=True)
    is_first_account=models.BooleanField(default=False)
    is_approve = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username+"  "+ self.accounts_type