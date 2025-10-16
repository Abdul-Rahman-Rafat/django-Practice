from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show/', views.show, name='show'),
    path('books/', views.show, name='show'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books_list/', views.books_list, name='books_list'),
]
