from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer

# Create your views here.

def noticeall(request):
    nall = Notice.objects.all()
    serializerdata = Noticeserializers(nall,many=True)
    json_data = JSONRenderer().render(serializerdata.data)
    return HttpResponse(json_data,content_type = "application/json")

def eventall(request):
    eall = Event.objects.all()
    serializerdata = Eventserializers(eall,many=True)
    json_data = JSONRenderer().render(serializerdata.data)
    return HttpResponse(json_data,content_type = "application/json")