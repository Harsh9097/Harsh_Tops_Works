from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render
from .models import *
from .forms import *
from .mixin import *
# from  transaction.models import Deposit
from django.views.generic import TemplateView,RedirectView,CreateView,ListView,UpdateView
from django.views.generic import DeleteView,DetailView , View
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from transaction.models import Transaction
from django.core.mail import send_mail
from service.email import *
from django.contrib import messages
from django.urls import reverse_lazy
import random
import string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse
from django.views.generic import View
from django_datatables_too.mixins import DataTableMixin
from django.db.models import Q
from User import tasks
from transaction.models import *
from django.urls import reverse_lazy , reverse


# Create your views here.


#permissions

class Visiterpage(TemplateView):
    template_name = "mainpage/visiter_page.html"

#Login
class LoginRedirectView(LoginRequiredMixin,RedirectView):
     
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.role=="Manager":
                return ManagerHomeView.as_view()(request, args, kwargs)
            elif request.user.role=="Staff":
                return StaffHomeView.as_view()(request, *args, kwargs)
            
            elif request.user.role=="Customer":
                return CustomerHomeView.as_view()(request, *args, kwargs)
           
        else:
            return HttpResponseRedirect('/accounts/login')

#Login Homepage
class ManagerHomeView(ManagerAccessMixin,TemplateView):
      template_name = "manager/M_index.html"
      def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff'] = User.objects.filter(role="Staff").filter(deleted = False).count()
        context['customer'] = User.objects.filter(role="Customer").filter(deleted = False).count()
        context['approves'] = User.objects.filter(is_active=False).filter(deleted = False).count()
        context['accounts'] = Account.objects.filter(is_approve=True).filter(deleted = False).count()
        context['pending_account'] = Account.objects.filter(is_approve=False).filter(deleted = False).count()

        return context

class StaffHomeView(StaffAccessMixin,TemplateView):
       template_name = "staff/S_index.html"
       def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['staff'] = User.objects.filter(role="Staff").filter(deleted = False).count()
            context['customer'] = User.objects.filter(role="Customer").filter(deleted = False).count()
            context['approves'] = Transaction.objects.filter(is_approve=False).filter(deleted = False).count()
            return context
        


class CustomerHomeView(CustomerAccessMixin,TemplateView):
       template_name = "customer/C_index.html"
       def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['Accounts_List'] = Account.objects.filter(user=self.request.user).filter(is_approve=True,deleted = False) 
            return context

       


#Staff Views

class StaffCreateView(ManagerAccessMixin,CreateView):
    model = User
    form_class =StaffForm
    template_name = "manager/add_staff.html"
    success_url="/staff_list/"

    
    def form_valid(self, form):
        form.instance.role="Staff"
        email=form.cleaned_data["email"]
        characters = string.ascii_letters + string.digits 
        password = ''.join(random.choice(characters) for i in range(1,10))
        form.instance.set_password(password)
        staff=form.save(commit=True)
        #mail
        print('Mail is sending to the Staff ')
        subject = "For Login as Staff,for your security purpose"
        from_email = 'admin@gmail.com'
        to_email = [staff.email]
        username = form.instance.username
        variable_dict = {"username":username,"password":password}
        tasks.send_email_add_staff.delay(subject,from_email,to_email, variable_dict=variable_dict)
        print('Mail is sent successfully')
        return super().form_valid(form)
       
    def form_invalid(self, form):
         print(form.errors)
         return super().form_invalid(form)
    
    
class Thankyou(LoginRequiredMixin,TemplateView):
    template_name = "manager/thank.html"



class StaffListView(ManagerAccessMixin,ListView):
    model = User
    template_name = "manager/staff_list.html"

  


class StaffAjaxView(DataTableMixin,View):
    model = User
    def get_queryset(self):
        qs = User.objects.all()
        if self.request.user:
            qs = User.objects.filter(role = "Staff").filter(deleted = False)
        return qs
    def _get_actions(self, obj):
        update_url= f'/staff_Update/{obj.pk}' 
        detail_url =f'/staff_detail/{obj.pk}'
       
        # return f'actions buttons'
        return f'<a href="{detail_url}"<button type="button" class="btn-sm btn btn-success"><span class="bi bi-eye"></span></button></a> <a href="{update_url}" <button type="button" class="btn-sm btn  btn-warning"><span class="bi bi-pen"></span></button></a> <button type="button" class="btn-sm btn btn-danger ajax-delete-staff-btn" data-id="{obj.pk}"><span class="bi bi-trash"></span></button>'
        
      
    
    def filter_queryset(self, qs):
        if self.search:
            return qs.filter(
                Q(id__icontains=self.search) |
                Q(username__icontains=self.search) |
                Q(first_name__icontains=self.search) |
                Q(last_name__icontains=self.search)|
                Q(email__icontains=self.search) |
                Q(gender__icontains=self.search) |
                Q(contact_number__icontains=self.search) |
                Q(dob__icontains=self.search) 


            )
        return qs

    def prepare_results(self, qs):
        data = []
        for o in qs:
            data.append({
                'id': o.id ,
                'username': o.username,
                'first_name': o.first_name,
                'last_name': o.last_name,
                'email': o.email,
                'gender': o.gender,
                'contact_number': o.contact_number,
                'dob': o.dob.strftime("%d-%B-%y"),
                'actions': self._get_actions(o),
            })
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)

    

class StaffUpdateView(ManagerAccessMixin,UpdateView):
    model = User
    form_class = StaffForm
    template_name = "manager/add_staff.html"
    success_url = "/staff_list/"


class StaffDetailsView(ManagerAccessMixin,DetailView):
    
    model = User
    template_name = "manager/staff_details.html"
    success_url = "/stafflist/"
    context_object_name = "staff"

class StaffDeleteView(ManagerAccessMixin,View):
    model = User
    template_name = "manager/delete.html"
    success_url = "/staff_list/"

    def post(self, request):
        id = request.POST.get('id')  
        user = User.objects.get(id = id)
        user.is_active=False
        user.delete()
    
        return JsonResponse({'message': 'Customer data deleted successfully'})





#Customer

class CustomerCreateView(CreateView):
    model = User
    form_class = CustomerForm 
    template_name = "customer/registration.html"
    success_url = "/accounts/login/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['AccountForm'] = AccountForm()
        context['template'] = "manager/simple.html" 
        return context


    def form_valid(self,form):
        form.instance.role="Customer"

        email=form.cleaned_data["email"]
        form_password = form.cleaned_data["password"]
        
        
        #for username 
        Usercharacters = string.ascii_letters + string.digits 
        username = ''.join(random.choice(Usercharacters) for i in range(1,6))
        form.instance.username=username

        form.instance.set_password(form_password)

        #Account no 
        account_no_characters =  string.digits 
        account_no = ''.join(random.choice(account_no_characters) for i in range(1,13))
       
        #save form
        user=form.save(commit=False)
        user.is_active = False
        
        user.save()

        type = self.request.POST['accounts_type']
        Account.objects.create(account_no=account_no, accounts_type=type, user=user, is_first_account=True,is_approve=True)

        print('Mail is sending to Customer')
        subject = "waiting for approval status"
        from_email = 'admin@gmail.com'
        to_email = [user.email]     
        tasks.customer_apply_account.delay(subject,from_email,to_email)
        print('Mail is sent successfully')
      
        return super().form_valid(form)
       

class CustomerListView(AccessMixin,ListView):
    model = User
    template_name = "manager/customer_list.html"
    context_object_name = "customer"





#data table 
class CustomerAjaxView(DataTableMixin,View):
    model = User
    def get_queryset(self):
        qs = User.objects.all()
        if self.request.user:
            qs = User.objects.filter(role = "Customer",deleted= False ,is_active=True)
        return qs


    def _get_actions(self, obj):
        """Get action buttons w/links."""
        update= f'/customer_Update/{obj.pk}'
        detail =f'/customer_detail/{obj.pk}'
     
        if self.request.user.role == "Manager":
            return f'<a href="{detail}"<button type="button" class="btn-sm btn btn-success "><span class="bi bi-eye"></span></button></a> <a href="{update}" <button type="button" class="btn-sm btn  btn-warning"><span class="bi bi-pen"></span></button></a> <button type="button" class="btn-sm btn btn-danger ajax-delete-btn" data-id="{obj.pk}"><span class="bi bi-trash"></span></button>'
    
        else:
             return f'<a href="{detail}"<button type="button" class="btn-sm btn btn-success "><span class="bi bi-eye"></span></button></a> <a href="{update}" <button type="button" class="btn-sm btn  btn-warning"><span class="bi bi-pen"></span></button></a>'
    def filter_queryset(self, qs):
        if self.search:
            return qs.filter(
                Q(id__icontains=self.search)|
                Q(first_name__icontains=self.search) |
                Q(last_name__icontains=self.search)|
                Q(email__icontains=self.search) |
                Q(username__icontains=self.search) |
                Q(gender__icontains=self.search) |
                Q(contact_number__icontains=self.search) |
                Q(dob__icontains=self.search) 


            )
        return qs

    def prepare_results(self, qs):
        # Create row data for data tables
        data = []
        for o in qs:
            data.append({
                'id': o.id ,
                'username': o.username,
                'first_name': o.first_name,
                'last_name': o.last_name,
                'adhar_no': o.adhar_no,
                'pan_no': o.pan_no,
                'email': o.email,
                'gender': o.gender,
                'contact_number': o.contact_number,
                'dob': o.dob.strftime("%d-%B-%y"),
                'actions': self._get_actions(o),
            })
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)


    
class CustomerDetailView(AccessMixin,DetailView):
    model = User
    template_name = "manager/customer_details.html"
    context_object_name = "customer"
    success_url = "/customer_list/"


class CustomerUpdateView(AccessMixin,UpdateView):
    model = User
    form_class = CustomerForm
    success_url = "/customer_list/"
    template_name = "customer/registration.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['AccountForm'] = AccountForm()
        context['template'] = "base.html" 

        return context


class CustomerDeleteView(ManagerAccessMixin,View):
    def post(self, request):
        id = request.POST.get('id')
        user = User.objects.get(id = id)
        accounts = Account.objects.filter(user =user)
        for account in accounts:
            accounts.deleted =  True
            accounts.is_approve =False
            account.delete()
        user.is_active=False
        user.delete()
        return JsonResponse({"message": "Vendor Document Deleted Successfully."})


#approve form:


class ApproveListView(ManagerAccessMixin,ListView):
    model = User
    template_name = "manager/approve.html"
    context_object_name = "approve"
    



class customer_approve_data_table(DataTableMixin,View):
    model =  User
    def get_queryset(self):
        qs = User.objects.all()
        if self.request.user:
            qs = User.objects.filter(is_active = False).filter(deleted = False)
        return qs

    def _get_actions(self, obj):
        return f'<button type="button" class="btn-sm btn btn-success btn-manager-action" data-action-id="{obj.id}" value="Approve">Approve</button> <button type="button" class="btn-sm btn btn-danger btn-manager-action" data-action-id="{obj.id}" value="DisApprove">DisApprove</button>'

    
    def filter_queryset(self, qs):
        
        if self.search:
                return qs.filter(
                    Q(id__icontains=self.search)|
                    Q(first_name__icontains=self.search) |
                    Q(last_name__icontains=self.search)|
                    Q(pan_no__icontains=self.search) |
                    Q(user_account__account_no__icontains=self.search) |
                    Q(adhar_no__icontains=self.search) 
                )
        return qs

    def prepare_results(self, qs):
        # Create row data for data tables
        data = []
        for o in qs:
            data.append({
                'id': o.id ,
                'first_name': o.first_name,
                'last_name': o.last_name,
                'accounts_type':o.user_account.first().accounts_type,
                'adhar_no': o.adhar_no,
                'pan_no': o.pan_no,
                'actions': self._get_actions(o),
            })
        return data


    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)
#approve for customer
class Customer_approve_action(ManagerAccessMixin,View):
    def post(self, request):
        action = request.POST.get('action')
        customer_id = request.POST.get('id')
     
        if action =='Approve':
            instance = User.objects.get(id=customer_id)
            account = Account.objects.get(user=instance, is_first_account = True)
            
            account.is_approve = True
            account.save()

            instance.is_active = True
            
            instance.save()
           
            print('Mail is sending to Customer')
            subject = "waiting for approval status"
            from_email = 'admin@gmail.com'
            to_email = [instance.email]

            account_no=  instance.user_account.first().account_no
            
            password = instance.password
            variable_dict = {"username":instance.username,"account_no":account_no}

            tasks.send_email_Approve_customer.delay(subject,from_email,to_email, variable_dict=variable_dict)
            print('Mail is sent successfully')
            
            return JsonResponse({'message': 'Customer Add successfully'})
        elif action == 'DisApprove':
            user = User.objects.get(id = customer_id)

            accounts = Account.objects.filter(user =user)
            for account in accounts:
                accounts.deleted =  True
                accounts.is_approve =False

            account.delete()

            
            user.delete()
            return JsonResponse({'message': 'Customer data deleted successfully'})

#Open Account
class Open_accountCreateView(CustomerAccessMixin,CreateView):
    model = Account
    form_class = OpenAccountForm
    template_name = "customer/add_account.html"

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["user"] = self.request.user
        return form_kwargs


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        new_account_no_characters =  string.digits 
        new_account_no = ''.join(random.choice(new_account_no_characters) for i in range(1,13))
        instance.account_no = new_account_no
        instance.is_approve = False
        instance.save()
        messages.add_message(self.request, messages.WARNING, "Wait for the Approve by Bank and  Your Account Number is send in your Email")
        return redirect(reverse_lazy('open-account'))


class approve_Accounts_ListView(ManagerAccessMixin,ListView):
    model = Account
    template_name = "manager/approve_accounts_list.html"

class Customer_Accounts_Approve_Data_Table(DataTableMixin,View):
    model =  Account
    def get_queryset(self):
        qs = Account.objects.all()
        if self.request.user:
            qs = Account.objects.filter(is_approve = False,deleted = False)
        return qs

    def _get_actions(self, obj):
        return f'<button type="button" class="btn-sm btn btn-success btn-manager-action" data-action-id="{obj.id}" value="Approve">Approve</button> <button type="button" class="btn-sm btn btn-danger btn-manager-action" data-action-id="{obj.id}" value="DisApprove">DisApprove</button>'

    
    def filter_queryset(self, qs):
        
        if self.search:
                return qs.filter(
                    Q(id__icontains=self.search)|
                    Q(user__first_name__icontains=self.search) |
                    Q(user__last_name__icontains=self.search)|
                    Q(account_no__icontains=self.search) |
                    Q(accounts_type__icontains=self.search) 

                )
        return qs

    def prepare_results(self, qs):
        # Create row data for data tables
        data = []
        for o in qs:
            data.append({
                'id': o.id ,
                'username':o.user.username,
                'first_name': o.user.first_name,
                'last_name': o.user.last_name,
                'account_no': o.account_no,
                'accounts_type':o.accounts_type,
                'actions': self._get_actions(o),
            })
        return data


    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)

class Account_approve_action(ManagerAccessMixin,View):
    model=Account
    def post(self, request):
        action = request.POST.get('action')
        account_id = request.POST.get('id')
     
        if action =='Approve':
            instance = Account.objects.get(id=account_id)
            instance.is_approve = True

            user=User.objects.get(user_account=instance)
            instance.save()
           
            print('Mail is sending to Customer')
            subject = "waiting for approval status"
            from_email = 'admin@example.com'
            to_email = [user.email]
            
            tasks.send_email_additional_account.delay(subject,from_email,to_email, account_no=instance.account_no)
            print('Mail is sent successfully')
            
            return JsonResponse({'message': 'Customer Account Add successfully'})
        elif action == 'DisApprove':
            user = Account.objects.get(id = account_id)
            user.is_approve = False

            user.delete()
            return JsonResponse({'message': 'Customer data deleted successfully'})

class Customer_account_ListView(ManagerAccessMixin,ListView):
    model = Account
    template_name = "manager/customer_account_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["account"] = Account.objects.all()
        context["accounts_type"] = Account.account_type
        return context
    
class Customer_account_list_data_table(DataTableMixin,View):
    model =  Account
    def get_queryset(self):
        qs = Account.objects.all()
        if self.request.user:
            qs = Account.objects.filter(is_approve = True,deleted = False)
        accounts_type_1 = self.request.GET.get('accounts_type')
        if accounts_type_1:
            qs = qs.filter(accounts_type = accounts_type_1)
        return qs

    def _get_actions(self, obj):
        return f'<button type="button" class="btn-sm btn btn-danger btn-manager-action" data-action-id="{obj.id}" value="DisApprove">Delete Account</button>'

    
    def filter_queryset(self, qs):
        
        if self.search:
                return qs.filter(
                    Q(id__icontains=self.search)|
                    Q(user__first_name__icontains=self.search) |
                    Q(user__last_name__icontains=self.search)|
                    Q(account_no__icontains=self.search) |
                    Q(accounts_type__icontains=self.search) 

                )
        return qs

    def prepare_results(self, qs):
        # Create row data for data tables
        data = []
        for o in qs:
            data.append({
                'id': o.id ,
                'username':o.user.username,
                'first_name': o.user.first_name,
                'last_name': o.user.last_name,
                'account_no': o.account_no,
                'accounts_type':o.accounts_type,
                'actions': self._get_actions(o),
            })
        return data


    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)




#profile page template 

class ManagerProfile(ManagerAccessMixin,TemplateView):
       template_name = "manager/m_profile.html"


class StaffProfile(StaffAccessMixin,TemplateView):
       template_name = "staff/s_profile.html"


class CustomerProfile(CustomerAccessMixin,TemplateView):
       template_name = "customer/c_profile.html"



  