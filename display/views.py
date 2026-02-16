from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

def index(request):
    if request.user.is_authenticated:
        return HttpResponse("You're an authenticated user! You're at the display index.")
    else:
        return HttpResponse("You're not authenticated. You're at the display index.")