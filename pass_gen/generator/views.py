from django.shortcuts import render
from django.http import HttpResponse
import random
import string


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    the_pass = '!'
    characters = list(string.ascii_lowercase)
    length = int(request.GET.get('length','12'))
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list(string.punctuation))
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))

    for x in range(length):
        the_pass += random.choice(characters)
    return render(request, 'generator/password.html', {'password': the_pass})


def eggs(request):
    return HttpResponse('<h1> Яйца </h1>')
