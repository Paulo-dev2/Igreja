from django.contrib import admin
from django.urls import path,include
from .views import login_view, register_user, logout_user

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", logout_user, name="logout"),
    path("", include("dashboard.home.urls")),
]
