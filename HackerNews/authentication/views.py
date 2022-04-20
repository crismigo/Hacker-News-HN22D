from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
'''def login(request):

    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            us = form.cleaned_data.get("username")
            pa = form.cleaned_data.get("password")
            user=authenticate(username=us, password=pa)
            if user is not None:
                login(request, user)
                return redirect('Home')

            else:
                messages.error(request, "Usuari erroni")
        else:

            messages.error(request, "Usuari erroni")

    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})'''

def logout(request):
    logout(request)

    return redirect(request.path)

def login(request):

    return redirect(accounts/login)