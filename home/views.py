from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hi(request):
    return render(request, 'home/Landing_Page.html')

def play(request):
    return render(request, 'home/play.html')

def forum(request):
    return render(request, 'home/forum.html')

def store(request):
    return render(request, 'home/store.html')

def check(request):
    return render(request, 'home/checkout.html')
