
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #Login redirect view 
    path('Dashboard', LoginRedirectView.as_view(), name='Dashboard'),
    path('', Visiterpage.as_view(), name='home'),
    #Manager
    path('manager/', ManagerHomeView.as_view(), name='manager'),
    path('tq/', Thankyou.as_view(), name='tq'),
    path('approve_list/', ApproveListView.as_view(), name='approvelist'),
    path('customer_approve_data_table/', customer_approve_data_table.as_view(), name='customer_approve_data_table'),
    path('customer_approve_action/', Customer_approve_action.as_view(), name='customer_approve_action'),
    path('manager_profile/',ManagerProfile.as_view(), name='managerprofile'),
    
    



    #Staff
    path('staff/', StaffHomeView.as_view(), name='staff'),
    path('add_staff/',StaffCreateView.as_view(), name='addstaff'),
    path('staff_list/',StaffListView.as_view(), name='stafflist'),
    path('staff_Update/<int:pk>',StaffUpdateView.as_view(), name='staffupdate'),
    path('staff_detail/<int:pk>',StaffDetailsView.as_view(), name='staffdetail'),
    path('staff_Detete/',StaffDeleteView.as_view(), name='staffdelete'),
    path('staff_profile/',StaffProfile.as_view(), name='staff_profile'),
   
  
 
   #Customer
    path('customer/', CustomerHomeView.as_view(), name='customer'),
    path('ragistration/',CustomerCreateView.as_view(), name='registration'),
    path('customer_profile/',CustomerProfile.as_view(), name='customer_profile'),
    path('customer_list/',CustomerListView.as_view(), name='customer_list'),
    path('customer_Update/<int:pk>',CustomerUpdateView.as_view(), name='customerupdate'),
    path('customer_detail/<int:pk>',CustomerDetailView.as_view(), name='customerdetail'),
    path('customer_Detete/',CustomerDeleteView.as_view(), name='customer_delete'),


    #Accounts
    path('open_account/',Open_accountCreateView.as_view(), name='open-account'),
    path('approve_accounts_list/',approve_Accounts_ListView.as_view(), name='approve_account_list'),
    path('customer_account_approve/',Customer_Accounts_Approve_Data_Table.as_view(), name='customer-accounts-approve'),
    path('account_approve_action/',Account_approve_action.as_view(), name='accounts-approve-action'),
    path('customer_Accounts/',Customer_account_ListView.as_view(), name='customer-accounts-list'),
    path('customer_Accounts_Data_table/',Customer_account_list_data_table.as_view(), name='customer-accounts-list-data_table'),
    

   #ajax staff list
   path('staff_list_ajax/',StaffAjaxView.as_view(), name='stafflist_ajax'),
   #ajax customer list
    path('customer_list_ajax/',CustomerAjaxView.as_view(), name='customer_list_ajax')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
