from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author

def home(request):
    return render(request, 'base.html')


def books_list(request):
    books = Book.objects.all()  
    return render(request, 'pages/books_list.html', {'books': books})

def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return render(request, 'pages/404.html', status=404)

    return render(request, 'pages/book_detail.html', {'book': book})
def show(request):
    books = Book.objects.all()
    return render(request, 'pages/show.html', {'lista': books})

def author(request, author_id):
    
    author = get_object_or_404(Author, id=author_id)
    books = author.books.all()
    return render(request, 'pages/author.html', {'author': author, 'books': books})


