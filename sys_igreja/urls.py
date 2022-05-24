from django.contrib import admin
from django.urls import path,include
from core import views
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.hello),
    path('dashboard/',include("dashboard.urls")),
    path('',RedirectView.as_view(url='/hello/'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
