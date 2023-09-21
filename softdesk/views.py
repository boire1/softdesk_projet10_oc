from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

from django.contrib.auth.views import LogoutView

