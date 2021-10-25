from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")

def webPage(request):
    return render(request, 'myApp/myApp.html')