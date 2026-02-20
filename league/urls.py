from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:slug>/", views.league, name="league"),
    path("join/<str:slug>", views.join, name="join"),
]