from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        # Get credentials from the form (e.g., request.POST['username'], request.POST['password'])
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verify credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in, which manages the session and cookie
            login(request, user)
            # Redirect to a success page
            return redirect('index')
        else:
            # Provide an error message
            return HttpResponse("Invalid login details")
    else:
        # Render the login form
        return render(request, 'user_profile/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        # Get credentials from the form (e.g., request.POST['username'], request.POST['password'])
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verify that the username isn't already taken.
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken")
        else:
            User.objects.create_user(username=username, password=password)
            return redirect('/login/')
    else:
        # Render the registration form
        return render(request, 'user_profile/register.html')
