from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from dashboard.views import Dashboard

urlpatterns = [
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")),
]
