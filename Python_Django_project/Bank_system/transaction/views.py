from typing import Any, Dict
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,RedirectView,CreateView,ListView,UpdateView,View ,FormView
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from requests import request
from django_datatables_too.mixins import DataTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from .mixin import *
from django.http import JsonResponse
from django.core.mail import send_mail
from service.email import *
from transaction import tasks


# Create your views here.

class DepositCreateView(CreateView):
    model = Transaction
    form_class = DepositForm
    template_name = "transaction/deposit.html"

    def get_success_url(self):
        return reverse("home")


    
class DepositListView(StaffAccessMixin,ListView):
    model = Transaction
    context_object_name="deposit"
    template_name = "transaction/Deposit_list.html"
    

  
class Deposit_data_table(DataTableMixin,View):
    model =  Transaction
    def get_queryset(self):
      return Transaction.objects.filter(is_approve = False).filter(deleted = False)

    def _get_actions(self, obj):
        return f'<button type="button" class="btn-sm btn btn-success btn-staff-action" data-action-id="{obj.id}" value="Approve">Approve</button> <button type="button" class="btn-sm btn btn-danger btn-staff-action" data-action-id="{obj.id}" value="DisApprove">DisApprove</button>'
         
    
    def filter_queryset(self, qs):
        if self.search:
            return qs.filter(
                Q(id__icontains=self.search) |
                Q(depositor_name__icontains=self.search) |
                Q(account_no__icontains=self.search)|
                Q(amount__icontains=self.search) |                    
                Q(contact_number__icontains=self.search)



            )
        return qs

    def prepare_results(self, qs):
        data = []
        for o in qs:
            data.append({
            
                 
                'id': o.id,
                'depositor_name': o.depositor_name,
                'account_no': o.account.account_no,
                'amount': o.amount,
                'contact_number': o.contact_number,
                'actions': self._get_actions(o) ,
            })
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)


class staff_action_deposit(View):
    def post(self, request):
        action = request.POST.get('action')
        deposit_id = request.POST.get('id')
        if action == 'DisApprove':
            user = Transaction.objects.get(id=deposit_id)
            user.delete()
            return JsonResponse({'success': True, 'message': 'Customer data deleted successfully'})
        elif action == 'Approve':
            deposit = Transaction.objects.get(id=deposit_id)
            print(deposit.account.account_no)

           
            if Account.objects.filter(account_no=deposit.account.account_no).exists():
                account = Account.objects.get(account_no=deposit.account.account_no)
                if account.balance is not None:
                    account.balance += deposit.amount
                    deposit.available_balance_after_transaction = account.balance

                else:
                    account.balance = deposit.amount

                deposit.is_approve = True
                account.save()
                deposit.save()
                print('Mail is sending to the Customer ')
                subject = "Credit mail"
                from_email = 'admin@gmail.com'
                to_email = [account.user.email]
                variable_dict = {"account_no":account.account_no,"amount":deposit.amount , "created_at":deposit.created_at ,"available_balance_after_transaction":deposit.available_balance_after_transaction}
                tasks.send_email_credit.delay(subject,from_email,to_email=to_email,variable_dict=variable_dict)
                return JsonResponse({'success': True, 'message': 'Customer deposit successful'})
            else:
                return JsonResponse({'success': False, 'message': 'Account number is wrong'})

# #withdraw

class WithdrawCreateView(CreateView):
    model = Transaction
    form_class = WithdrawForm
    template_name = "transaction/withdraw.html"
    def form_valid(self, form):
        account_number = form.cleaned_data["account_no"]
        user_amount = form.cleaned_data["amount"]
        pin = form.cleaned_data["security_pin"]

        
        account = Account.objects.get(account_no=account_number)

        account.balance -= user_amount
        account.save()

        withdrawn = Transaction.objects.create(
            account=account,
            account_holder_name=account.user.first_name,
            amount=user_amount,
            available_balance_after_transaction=account.balance,
            contact_number=account.user.contact_number,
            transactions_type=Transaction.DEBIT
        )
        withdrawn.is_approve=True
        withdrawn.save()
    
        print('Mail is sending to the Staff ')
        subject = "Debit mail"
        from_email = 'admin@gmail.com'
        to_email = [account.user.email]
        variable_dict = {"account_no":account.account_no,"amount":user_amount , "created_at":withdrawn.created_at ,"available_balance_after_transaction":withdrawn.available_balance_after_transaction}
        tasks.send_email_debit.delay(subject,from_email,to_email,variable_dict=variable_dict)
        print('Mail is sent successfully')
        return redirect(reverse_lazy('home'))
       


class PinView(CustomerAccessMixin,FormView):
    form_class =CreatePinForm
    template_name = "transaction/create_pin.html"
    context_object_name = "pin"

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["user"] = self.request.user
        return form_kwargs

    def form_valid(self, form):
        security_pin = form.cleaned_data['security_pin']
        account_number = form.cleaned_data['account_no']

        account_number = Account.objects.get(account_no = account_number)
        account_number.security_pin = security_pin
        
        account_number.save()
        
        return redirect(reverse("Dashboard"))


class PinView_ajax(View):
    def get(self, request):
        account_number = Account.objects.get(user=self.request.user, accounts_type=request.GET['account_type']).account_no
        return JsonResponse({'account_number':account_number})

  
         
         
 #Transaction

class TransactionListView(CustomerAccessMixin,ListView):
    model = Transaction
    context_object_name = "transactions"
    template_name = "transaction/transaction_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["account"] = Account.objects.all()
        context["accounts_type"] = Account.account_type
        return context

class Transaction_Data_table(DataTableMixin,View):
    model =  Transaction
    def get_queryset(self):
         queryset = super().get_queryset()
         queryset = queryset.filter(is_approve=True,deleted=False, account__user=self.request.user)
         return queryset
    
          
    def filter_queryset(self, qs):
        accounts_type_1 = self.request.GET.get('accounts_type')
        if accounts_type_1:
            qs = qs.filter(account__accounts_type = accounts_type_1)
        if self.search:
            return qs.filter(
                Q(id__icontains=self.search) |
                Q(account__user__first_name__icontains=self.search) |
                Q(account__account_no__icontains=self.search)|
                Q(transactions_type__icontains=self.search) |                
                Q(amount__icontains=self.search)|
                Q(created_at__icontains=self.search)|
                Q(available_balance_after_transaction__icontains=self.search)



            )
        return qs

    def prepare_results(self, qs):
        data = []
        for o in qs:
                data.append({
                'id': o.id,
                'user':o.account.user.first_name,
                'account_no': o.account.account_no,
                'transactions_type': o.transactions_type,
                'amount': o.amount,
                'date': o.created_at,
                'available_balance_after_transaction': o.available_balance_after_transaction,

        
               
            })
       
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)


 #Transfer
class TransferCreateView(CustomerAccessMixin,CreateView):
    model = Transaction
    form_class = TransferForm
    template_name ="transaction/transfer.html"

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["user"] = self.request.user
        return form_kwargs
    

    def form_valid(self, form):

        from_account = form.cleaned_data["from_account_number"]
        to_account = form.cleaned_data["to_account_number"]
        amount = form.cleaned_data["amount"]

        from_account.balance -= amount
        from_account.save()
        from_user_withdrawn = Transaction.objects.create(account=from_account, to_account_number=to_account.account_no, account_holder_name=from_account.user.first_name, amount=amount, depositor_name=from_account.user.first_name, available_balance_after_transaction=from_account.balance, contact_number=from_account.user.contact_number, transactions_type=Transaction.DEBIT)
        from_user_withdrawn.is_approve=True
        from_user_withdrawn.save()

        #Mail
        print('Mail is sending to the customer')
        subject = "Debit mail"
        from_email = 'admin@gmail.com'
        to_email = [from_user_withdrawn.account.user.email]
        variable_dict = {"account_no":from_user_withdrawn.account.account_no,"amount":amount , "created_at":from_user_withdrawn.created_at ,"available_balance_after_transaction":from_user_withdrawn.available_balance_after_transaction}
        tasks.send_email_debit.delay(subject,from_email,to_email,variable_dict=variable_dict)
        print('Mail is sent successfully')

        to_account.balance += amount
        to_account.is_approve= True
        to_account.save()
        to_user_deposited = Transaction.objects.create(account=to_account, account_holder_name=to_account.user.first_name, amount=amount, depositor_name=from_account.user.first_name, available_balance_after_transaction=to_account.balance, contact_number=from_account.user.contact_number, transactions_type=Transaction.CREDIT)
        to_user_deposited.is_approve=True
        to_user_deposited.save()
        messages.add_message(self.request, messages.SUCCESS, "your transaction is successful !")

        #mail
        print('Mail is sending to the Customer')
        subject = "Credit mail"
        from_email = 'admin@gmail.com'
        to_email = [to_user_deposited.account.user.email]
        variable_dict = {"account_no":to_user_deposited.account.account_no,"amount":amount , "created_at":to_user_deposited.created_at ,"available_balance_after_transaction":to_user_deposited.available_balance_after_transaction}
        tasks.send_email_credit.delay(subject,from_email,to_email,variable_dict=variable_dict)
        print('Mail is sent successfully')
        return redirect(reverse_lazy('transfer'))


class transfer_ajax(View):
    def get(self, request):
        account_number = Account.objects.get(user=self.request.user, accounts_type=request.GET['account_type']).account_no
        return JsonResponse({'account_number':account_number})



