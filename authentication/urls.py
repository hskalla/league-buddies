from django.urls import path, include
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("password-change/", views.password_change, name="password change"),
    path("password-change/confirm/", views.password_change_confirm, name="password change confirm"),
]