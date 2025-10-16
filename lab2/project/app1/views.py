from django.shortcuts import render,redirect



# Create your views here.
def home(request):
    return render(request, 'base.html')

def show(request):
    lista = [
        {'name': "abdo", 'id': 1},
        {'name': "ali", 'id': 2},
        {'name': "ahmed", 'id': 3},
    ]
    return render(request, 'pages/show.html', {'lista': lista})
# views.py

# Simulated data (in-memory)
lista = [
    {'name': 'abdo', 'id': 1},
    {'name': 'ali', 'id': 2},
    {'name': 'ahmed', 'id': 3},
]

def show(request):
    return render(request, 'pages/show.html', {'lista': lista})

def delete(request, id):
    global lista
    lista = [item for item in lista if item['id'] != id]
    # Render the updated list directly instead of redirecting
    return render(request, 'pages/show.html', {'lista': lista})

