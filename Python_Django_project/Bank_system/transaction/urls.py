from django.urls import path
from .views import *

urlpatterns = [
      #Deposit
      path('deposit/', DepositCreateView.as_view(), name='deposit'),
      path('deposit_list/', DepositListView.as_view(), name='deposit_list'),
#     #   path('staffapprove/<int:pk>/', staffApproveView.as_view(), name='staffapprove'),
#     #   path('disapprove_deposit', Disaprove.as_view(), name='disapprove_deposit'),
      path('deposit_ajax_data_table/',Deposit_data_table.as_view(), name='deposit_data_table'),
      path('staff_action_deposit', staff_action_deposit.as_view(), name='Staff_action_deposit'),
     
 
#      #withdraw                  
        path('withdraw/', WithdrawCreateView.as_view(), name='withdraw'),
        path('create_pin/', PinView.as_view(), name='create_pin'),
        path('create_pin_ajax/', PinView_ajax.as_view(), name='create_pin_ajax'),
#      #Transaction
      path('transaction_list/', TransactionListView.as_view(), name='transaction'),
      path('transaction_data_table/', Transaction_Data_table.as_view(), name='transaction_Data_table'),
      
#      #Transfer 
      path('transfer/',TransferCreateView.as_view(), name='transfer'),
      path('transfer_ajax/',transfer_ajax.as_view(), name='transfer_ajax'),
]