from django.urls import path
from .views import *
urlpatterns = [
    
    path('base/', home,name='home'),
    path('show/', show,name='show'),
    path('delete/<int:id>/', delete, name='delete'),
    
    
]