from django.shortcuts import render



# Create your views here.

def fun1(request,name):
    return render(request, 'app1.html', {'name': name})