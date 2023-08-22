from django.shortcuts import render
from django.http import HttpResponse

import random
# Create your views here.

def home(request):
    return render(request, "generator/home.html")

def about(request):
    #return HttpResponse("Hello About")
    return render(request, "generator/about.html")

def password(request):
    characters = list('abcdefghijklmnñoprstuvwxyz')
    generate_password = ""

    #lee lo que llega por el navegador
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!#$%&/()=-_.'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    for char in range(length):
        generate_password += random.choice(characters)

    return render(request, "generator/password.html", {'password': generate_password})