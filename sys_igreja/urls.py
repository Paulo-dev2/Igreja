from django.contrib import admin
from django.urls import path,include
from core.views import User
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',include("dashboard.urls")),
    path('home/',User.home),
    path('agendas/',User.agendas),
    path('eventos/',User.eventos),
    path('blog/',User.blog),
    path('blog/<int:id>',User.blog_detail),
    path('sobre-nos/',User.sobreNos),
    path('contato/',User.contato),
    path('contato/submit/',User.contatoSubmit),
    path('',User.home),
]

handler404 = 'core.views.Erro404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
