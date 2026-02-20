from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("league.urls")),
    path("accounts/", include("authentication.urls")),
    path('admin/', admin.site.urls),
]
