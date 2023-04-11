from django.shortcuts import render
from .models import *
from .serializers import Bookserializers
from django.http import HttpResponse
from rest_framework.decorators import api_view
 
from rest_framework.renderers import JSONRenderer

# Create your views here.
@api_view(['GET'])
def bookall(request):
    ball = Book.objects.all() 
    serializerdata = Bookserializers(ball,many = True)
    josn_data = JSONRenderer().render(serializerdata.data)
    return HttpResponse(josn_data,content_type="application/json")

def add_book(request):
    if request.POST:
        title= request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        publisher = request.POST['publisher']

        bid= Book.objects.create(title= title , author =  author , isbn =  isbn , publisher =  publisher)
        
    return render(request,"myapp/index.html")