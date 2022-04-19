from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


# Create your views here.
from authentication.models import User


def loginView(request):
    user = User.objects.get(username="admin")
    login(request,user)
    return redirect(request.META.get('HTTP_REFERER'))


def logoutView(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))
