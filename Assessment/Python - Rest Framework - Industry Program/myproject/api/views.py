from django.shortcuts import render
from .models import *
from .serializers import Studnetserializers
from django.http import HttpResponse
from rest_framework.decorators import api_view

from rest_framework.renderers import JSONRenderer
# Create your views here.

@api_view(['GET'])
def studnetall(request):
    sall = Studnet.objects.all() #complex data - data quertyset 
    serializerdata = Studnetserializers(sall,many = True)# convert into python data type
    josn_data = JSONRenderer().render(serializerdata.data)
    return HttpResponse(josn_data,content_type="application/json")

def specificstudent(request,id):
    sdata =  Studnet.objects.get(id=id)
    serializerData = Studnetserializers(sdata)
    json_data = JSONRenderer().render(serializerData.data)
    return HttpResponse(json_data,content_type = "application/json")