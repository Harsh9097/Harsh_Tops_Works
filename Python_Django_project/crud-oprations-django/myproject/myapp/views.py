from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect
# Create your views here.
"""
1)To store data in model:-
==>models.objects.create(fieldname = value)

2)To fetch all data from model
==>models.objects.all()

3)fetch specific data from condition wise from the model(result expected queryset)
===>models.objects.filter(fieldname = searchvalue )

"""
def home(request):
    return render(request,"myapp/index.html")

def add_student(request):
    if request.POST:
        name = request.POST['name']
        city = request.POST['city']

        sid= student.objects.create(name = name,city = city)
        
    return render(request,"myapp/index.html")

def all_student(request):
    sall = student.objects.all()
    print("============>sall",sall)
    context ={
        'sall' : sall
    }
    return render(request,"myapp/all-student.html",context)

def search_student(request):
    if request.POST:
        cityname =  request.POST['city']
        sall= student.objects.filter(city = cityname)
        print("===============>sall",sall)
        context ={
            'sall' : sall
        }
        return render(request,"myapp/all-student.html",context)
    else:
        sall= student.objects.all()
        print("===============>sall",sall)
        context ={
            'sall' : sall
        }
        return render(request,"myapp/all-student.html",context)

def del_student(request,pk):
    sid = student.objects.get(id = pk)
    print("===================>sid",sid)
    sid.delete()
    return redirect("all-student")

def update_student(request,id):
    sid = student.objects.get(id = id)
    context ={
        'sid' : sid
    }
    return render(request,"myapp/update.html",context)

def change_student(request):
    if request.POST:
        id   =   request.POST['id']
        name = request.POST['name']
        city = request.POST['city']

        sid=student.objects.get(id = id)
        sid.name = name 
        sid.city = city 
        sid.save()
        return redirect("all-student")