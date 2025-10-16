from django.urls import path
from . import views

urlpatterns = [
    
path('fun2/<name>', views.fun2)    
]