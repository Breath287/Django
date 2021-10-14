from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def listorders(request):
    return HttpResponse('Order information are listed below: ')
