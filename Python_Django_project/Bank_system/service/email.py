# from User.models import *
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives

# class EmailSender:
#     def send_email_custom(subject,from_email,to_email,variable_dict):
#         html_content = render_to_string("manager/Approve_email.html", variable_dict)
#         email = EmailMultiAlternatives(subject,html_content,from_email,to_email)
#         email.send()

# class Staff_send:
#     def send_email_custom(subject,from_email,to_email,variable_dict):
#         html_content = render_to_string("manager/staff_email.html", variable_dict)
#         email = EmailMultiAlternatives(subject,html_content,from_email,to_email)
#         email.send()

# class Customer_send:
#         def send_email(subject,from_email,to_email):
#             html_content = render_to_string("manager/apply_account_email.html")
#             email = EmailMultiAlternatives(subject,html_content,from_email,to_email)
#             email.send()    

# class Customer_disapprove:
#     def send_email(subject,from_email,to_email):
#             html_content = render_to_string("manager/customer_disapprove_email.html")
#             email = EmailMultiAlternatives(subject,html_content,from_email,to_email)
#             email.send()  

# class Account_Approve:
#     def send_email_Account(subject,from_email,to_email,account_no):
#             context={

#             }
#             context['account_no'] = account_no
#             html_content = render_to_string("manager/Account_email.html",context = context)
#             email = EmailMultiAlternatives(subject,html_content,from_email,to_email)
#             email.send()  

# class Debit:
#     def send_email_debit(subject,from_email,to_email,variable_dict):
#             html_content = render_to_string("customer/debit_mail.html",context = variable_dict)
#             email = EmailMultiAlternatives(subject,html_content,from_email,to_email,variable_dict)
#             email.send()  

# class Credit:
#     def send_email_credit(subject,from_email,to_email,variable_dict):
#             html_content = render_to_string("customer/credit_mail.html",variable_dict)
#             email = EmailMultiAlternatives(subject,html_content,from_email,to_email)
#             email.send()  

