from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(req):
    return HttpResponse('anasayfa')

def emrePage(request):
    return HttpResponse('emre sayfa')
