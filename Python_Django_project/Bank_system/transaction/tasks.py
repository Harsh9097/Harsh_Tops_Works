from User.models import *
from transaction.models import *
from Bank_system.celery import app
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives



@app.task()
def send_email_credit(subject,from_email,to_email,variable_dict):
        html_content = render_to_string("customer/credit_mail.html",variable_dict)
        email = EmailMultiAlternatives(subject,html_content,from_email,to_email)
        email.send()  

@app.task
def send_email_debit(subject,from_email,to_email,variable_dict):
            html_content = render_to_string("customer/debit_mail.html",context = variable_dict)
            email = EmailMultiAlternatives(subject,html_content,from_email,to_email,variable_dict)
            email.send()  
