from django.shortcuts import render

# Create your views here.

def python(request):
    return render(request,'python.html')

def kirak(request):
    return render(request,'kirak.html')