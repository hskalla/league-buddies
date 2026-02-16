from django.contrib import admin
from user_profile.views import login_view, logout_view, register_view
from django.urls import path, include


urlpatterns = [
    path("", include("display.urls")),
    path("login/", login_view),
    path("logout/", logout_view),
    path("register/", register_view),
    path('admin/', admin.site.urls),
]
