from django.db import models
from base.mymodels import BaseModel
from User.models import *
# # Create your models here.
class Transaction(BaseModel):
    CREDIT = "Credit"
    DEBIT = "Debit"
   


    # TRANSACTION_TYPE = ((DEPOSIT, DEPOSIT), (WITHDRAW, WITHDRAW) , (TRANSFER , TRANSFER ), (TRANSACTION , TRANSACTION))
    TRANSACTION_TYPE_CHOICES =(
            (CREDIT ,'Credit'),
            (DEBIT , 'Debit'),
          
    ) 
    account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_transaction")
    to_account_number  = models.CharField(null=True,blank=True)
    account_holder_name= models.CharField(max_length=50,null=True,blank=True) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    depositor_name = models.CharField(max_length=100)
    available_balance_after_transaction = models.BigIntegerField(null=True,blank=True)  
    contact_number = models.CharField()
    transactions_type = models.CharField(max_length=20,choices=TRANSACTION_TYPE_CHOICES)

    is_approve = models.BooleanField(default=False)

