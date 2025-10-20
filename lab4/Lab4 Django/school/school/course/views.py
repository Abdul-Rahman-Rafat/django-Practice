from django.shortcuts import render

# Create your views here.
def course_home(request):
    return render(request, 'course_home.html')
