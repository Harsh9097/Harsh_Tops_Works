from User.models import *
from transaction.models import *
from Bank_system.celery import app
from service.email import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives



@app.task()
def send_email_Approve_customer(subject,from_email,to_email,variable_dict):
        html_content = render_to_string("manager/Approve_email.html", variable_dict)
        email = EmailMultiAlternatives(subject,html_content,from_email,to_email)
        email.send()

@app.task()
def send_email_add_staff(subject,from_email,to_email,variable_dict):
        html_content = render_to_string("manager/staff_email.html", variable_dict)
        email = EmailMultiAlternatives(subject,html_content,from_email,to_email)
        email.send()

@app.task()
def customer_apply_account(subject,from_email,to_email):
        html_content = render_to_string("manager/apply_account_email.html")
        email = EmailMultiAlternatives(subject,html_content,from_email,to_email)
        email.send()    


@app.task()
def send_email_additional_account(subject,from_email,to_email,account_no):
        context={

        }
        context['account_no'] = account_no
        html_content = render_to_string("manager/Account_email.html",context = context)
        email = EmailMultiAlternatives(subject,html_content,from_email,to_email)
        email.send()  
