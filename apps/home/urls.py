# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home.api.views import Dashboard
from apps.home.pages.views import Pages

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('login/',Pages.login),


    path('pages/add-agenda/', Pages.addAgenda),
    path('pages/add-oferta/', Pages.addOferta),
    path('pages/add-dizimo/', Pages.addDizimo),
    path('pages/add-post/submit', Pages.addPostData),
    path('pages/add-post/',Pages.addPost),


    path('pages/listar-agenda/', Pages.listaAgenda),
    path('pages/listar-oferta/', Pages.listarOferta),
    path('pages/listar-dizimo/', Pages.listarDizimo),
    path('pages/listar-post/', Pages.ListarPost),
    path('details-post/<int:id>', Pages.DetailPost),


    path('pages/editar-agenda/<int:id>', Pages.editarAgenda),
    path('pages/editar-dizimo/<int:id>', Pages.editarDizimo),
    path('pages/editar-oferta/<int:id>', Pages.editarOferta),
    path('pages/editar-post/<int:id>', Pages.editarPost),


    path("add-agenda/",Dashboard.add_agendas),
    path("add-dizimo/",Dashboard.add_dizimo),
    path("add-oferta/",Dashboard.add_oferta),


    path("deletar/agenda/<int:id>",Dashboard.deletar_agenda),
    path("deletar/dizimo/<int:id>",Dashboard.deletar_dizimo),
    path("deletar/oferta/<int:id>",Dashboard.deletar_oferta),
    path("deletar/post/<int:id>",Dashboard.deletar_post),


    path('editar-agenda/', Dashboard.EditarAgenda),
    path('editar-dizimo/', Dashboard.EditarDizimo),
    path('editar-oferta/', Dashboard.EditarOferta),
    path('pages/editar-post/submit', Pages.addPostData),
]
