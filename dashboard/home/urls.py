# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from . import views
from dashboard.home.api.views import Dashboard
from dashboard.home.pages.views import Pages

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('login/',Pages.login),


    path('pages/add-agenda/', Pages.addAgenda),
    path('pages/add-oferta/', Pages.addOferta),
    path('pages/add-dizimo/', Pages.addDizimo),
    path('pages/add-post/submit', Pages.addPostData),
    path('pages/add-post/',Pages.addPost),
    path('pages/add-evento/',Pages.addEventos),
    path('pages/add-evento/submit', Pages.addEvento),
    path('pages/add-slide/', Pages.addSlide),
    path('pages/add-slide/submit', Pages.addSlideData),
    path('pages/add-user/', Pages.addUserData),
    path('pages/add-user/submit', Pages.addUserData),



    path('pages/listar-agenda/', Pages.listaAgenda),
    path('pages/listar-oferta/', Pages.listarOferta),
    path('pages/listar-dizimo/', Pages.listarDizimo),
    path('pages/listar-post/', Pages.ListarPost),
    path('pages/listar-evento/', Pages.ListarEvento),
    path('pages/listar-feedback/', Pages.ListaFeedback),
    path('pages/listar-slide/',Pages.ListaSlides),
    path('pages/listar-user/', Pages.ListarUser),
    
    path('details-post/<int:id>', Pages.DetailPost),
    path('details/feedback/<int:id>', Pages.DetailsFeedback),

    path('pages/editar-agenda/<int:id>', Pages.editarAgenda),
    path('pages/editar-dizimo/<int:id>', Pages.editarDizimo),
    path('pages/editar-oferta/<int:id>', Pages.editarOferta),
    path('pages/editar-post/<int:id>', Pages.editarPost),
    path('pages/editar-evento/<int:id>', Pages.editarEvento),
    path('pages/editar-slide/<int:id>', Pages.editarSlide),
    path('pages/editar-user/<int:id>', Pages.EditarUser),


    path("add-agenda/",Dashboard.add_agendas),
    path("add-dizimo/",Dashboard.add_dizimo),
    path("add-oferta/",Dashboard.add_oferta),


    path("deletar/agenda/<int:id>",Dashboard.deletar_agenda),
    path("deletar/dizimo/<int:id>",Dashboard.deletar_dizimo),
    path("deletar/oferta/<int:id>",Dashboard.deletar_oferta),
    path("deletar/post/<int:id>",Dashboard.deletar_post),
    path("deletar/evento/<int:id>",Dashboard.deletar_evento),
    path("deletar/feedback/<int:id>",Dashboard.deletar_feedback),
    path("deletar/slide/<int:id>",Dashboard.deletar_slide),
    path('deletar/user/<int:id>', Dashboard.DeleteUser),

    path('editar-agenda/', Dashboard.EditarAgenda),
    path('editar-dizimo/', Dashboard.EditarDizimo),
    path('editar-oferta/', Dashboard.EditarOferta),
    path('pages/editar-post/submit', Pages.addPostData),
    path('pages/editar-evento/submit', Pages.addEvento),
    path('pages/editar-slide/submit', Pages.addSlideData),
    path('pages/editar-user/submit', Pages.EditarUserData),

    path('pages/profile',Pages.Profile),
    path('pages/profile/submit',Pages.ProfileData)
]
