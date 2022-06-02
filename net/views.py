from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'net/index.html', {})

def sign_up(request):
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})
