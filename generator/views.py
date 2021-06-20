from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
        return render(request, 'generator/home.html')

def password(request):

        password = ''

        characters = list('abcdefjhigklmnopqrstuvwxyz')

        length = int(request.GET.get('length', 12))

        if request.GET.get('uppercase'):
                characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

        if request.GET.get('numbers'):
                characters.extend(list('1234567890'))
        
        if request.GET.get('special'):
                characters.extend(list("&é'(-è_ç),;.<>§/?:!ù*$^@^\=+-|{~#[`\]}£"))

        for i in range(length):
                password += random.choice(characters)

        return render(request, 'generator/password.html', {'password': password})

def about(request):
        return render(request, 'generator/about.html')
