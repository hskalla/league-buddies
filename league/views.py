from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.conf import settings

from .models import League, Game
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        return HttpResponse("You're an authenticated user! You're at the league index.")
    else:
        return HttpResponse("You're not authenticated. You're at the league index.")

@login_required
def league(request, slug):
    l = get_object_or_404(League, slug=slug)
    u = request.user
    # parse form submission
    if request.method == "POST":
        if 'log_game_submit' in request.POST:
            game_agent = u
            game_patient = User.objects.get(username=request.POST.get("opponent"))
            if request.POST.get("win"):
                game_win = True
            else:
                game_win = False
            # print(game_agent," (",type(game_agent),") ",game_patient," (",type(game_patient),") ",game_win, " (",type(game_win),")")
            game = Game(agent=game_agent,patient=game_patient,league=l,win=game_win)
            game.save()
        elif 'confirm_game_submit' in request.POST:
            game = Game.objects.get(id=request.POST.get("game"))
            # print(request.POST.get("game")," (",type(request.POST.get("game")),") ",request.POST.get("confirm_game_submit")," (",type(request.POST.get("confirm_game_submit")),")")
            if request.POST.get("confirm_game_submit") == "confirm":
                game.confirmed = True
                game.save()
            else:
                game.delete()
    return render(request, "league/league.html", {"league": l, "user": u})

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