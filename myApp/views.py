from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello!')

def My_name(request):
    context = {
        'name': 'Kobz'
    }
    return render(request, 'myApp/myApp.html', context)