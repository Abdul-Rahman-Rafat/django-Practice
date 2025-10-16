from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def fun2(request,name):
    
    return render( request, 'app2.html', {'name': name})