from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.conf import settings

from .models import League

def index(request):
    if request.user.is_authenticated:
        return HttpResponse("You're an authenticated user! You're at the league index.")
    else:
        return HttpResponse("You're not authenticated. You're at the league index.")

@login_required
def league(request, slug):
    l = get_object_or_404(League, slug=slug)
    return render(request, "league/league.html", {"league": l})

@login_required
def join(request, slug):
    l = get_object_or_404(League, slug=slug)
    if request.method == 'POST':
        # Add user to the league if they confirm
        user = request.user
        l.users.add(user)
        return redirect('league',slug=slug)
    else:
        # Render the registration form
        return render(request, "league/join.html", {"league": l})