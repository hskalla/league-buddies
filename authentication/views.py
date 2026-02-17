from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def login(request):
    if request.method == 'POST':
        # Get credentials from the form (e.g., request.POST['username'], request.POST['password'])
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verify credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in, which manages the session and cookie
            auth_login(request, user)
            # If the request contains a "next" flag, return to that page.
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect('index')
        else:
            # Provide an error message
            return HttpResponse("Invalid login details")
    else:
        # Render the login form
        return render(request, 'authentication/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def password_change(request):
    return HttpResponse("password change")

def password_change_confirm(request):
    return HttpResponse("password change confirm")