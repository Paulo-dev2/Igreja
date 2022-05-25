# -*- encoding: utf-8 -*-
from django import template
from django.http import JsonResponse
#from rest_framework import status
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from core.models import Agenda,Evento,Dizimo,Oferta,Post
from datetime import datetime
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

class Dashboard:
    @login_required(login_url="/dashboard/login/")
    def add_agendas(req):
        if req.method == 'POST':
            print(req.POST)
            nome_agenda = req.POST.get('nome_agenda')
            data_agenda_start = req.POST.get('data_agenda_start')
            token = req.POST.get('csrfmiddlewaretoken')
            print(data_agenda_start)
            if not token: 
                return HttpResponse({
                    "err":"Não existe token"
                })
            if data_agenda_start:
                if nome_agenda: 
                    if len(nome_agenda) < 4:
                            return JsonResponse({
                            "err":"Tamanho do nome agenda muito pequena"
                        },safe=False)
                    else:
                        Agenda.objects.create(name=nome_agenda,data_start=data_agenda_start)
                        return JsonResponse({
                            "sucess":"Criado com sucesso"
                        },safe=False)
                else:
                    return JsonResponse({
                        "err":"Nome agenda vazio"
                    },safe=False)
            else:
                return JsonResponse({
                    "err":"Data e horario de inicio inicio vazio"
                },safe=False)

    @login_required(login_url="/dashboard/login/")
    def deletar_agenda(req,id):
        if req.method == "GET":
            
            if id != 0:
                Agenda.objects.filter(id=id).delete()
                return redirect("/dashboard/pages/listar-agenda")
            return redirect("/dashboard/pages/listar-agenda")

    @login_required(login_url="/dashboard/login/")
    def EditarAgenda(req):
        if req.method == 'POST':
            
            nome_agenda = req.POST.get('nome_agenda')
            data_agenda_start = req.POST.get('data_agenda_start')
            id = req.POST.get('id')
            token = req.POST.get('csrfmiddlewaretoken')
            print(data_agenda_start)
            if not token: 
                return HttpResponse({
                    "err":"Não existe token"
                })
            if data_agenda_start:
                if nome_agenda: 
                    if len(nome_agenda) < 4:
                            return JsonResponse({
                            "err":"Tamanho do nome agenda muito pequena"
                        },safe=False)
                    else:
                        Agenda.objects.filter(id=id).update(name=nome_agenda,data_start=data_agenda_start)
                        return JsonResponse({
                            "sucess":"Editado com sucesso"
                        },safe=False)
                else:
                    return JsonResponse({
                        "err":"Nome agenda vazio"
                    },safe=False)
            else:
                return JsonResponse({
                    "err":"Data e horario de inicio inicio vazio"
                },safe=False)     


    @login_required(login_url="/dashboard/login/")
    def add_dizimo(req):
        if req.method == 'POST':
            nome = req.POST.get('nome')
            cpf = req.POST.get('cpf')
            tel = req.POST.get('tel')
            valor = req.POST.get('value')
            token = req.POST.get('csrfmiddlewaretoken')

            if not token: 
                return HttpResponse({
                    "err":"Não existe token"
                })
            if cpf and valor:
                if nome and tel: 
                    if len(nome) < 4:
                            return JsonResponse({
                            "err":"Tamanho do nome agenda muito pequena"
                        },safe=False)
                    else:
                        Dizimo.objects.create(name=nome,cpf=cpf,tel=tel,value=valor)
                        return JsonResponse({
                            "sucess":"adicionado com sucesso com sucesso"
                        },safe=False)
                else:
                    return JsonResponse({
                        "err":"Está faltando nome ou telefone"
                    },safe=False)
            else:
                return JsonResponse({
                    "err":"Está faltando cpf ou valor"
                },safe=False)

    @login_required(login_url="/dashboard/login/")
    def EditarDizimo(req):
        if req.method == 'POST':
            print(req.POST)
            nome = req.POST.get('nome')
            cpf = req.POST.get('cpf')
            tel = req.POST.get('tel')
            valor = req.POST.get('value')
            id = req.POST.get('id')
            token = req.POST.get('csrfmiddlewaretoken')

            if not token: 
                return HttpResponse({
                    "err":"Não existe token"
                })
            if cpf and valor:
                if nome and tel: 
                    if len(nome) < 4:
                            return JsonResponse({
                            "err":"Tamanho do nome agenda muito pequena"
                        },safe=False)
                    else:
                        Dizimo.objects.filter(id=id).update(name=nome,cpf=cpf,tel=tel,value=valor)
                        return JsonResponse({
                            "sucess":"Editado com sucesso com sucesso"
                        },safe=False)
                else:
                    return JsonResponse({
                        "err":"Está faltando nome ou telefone"
                    },safe=False)
            else:
                return JsonResponse({
                    "err":"Está faltando cpf ou valor"
                },safe=False) 
    
    @login_required(login_url="/dashboard/login/")
    def deletar_dizimo(req,id):
        if req.method == "GET":
            
            if id != 0:
                Dizimo.objects.filter(id=id).delete()
                return redirect("/dashboard/pages/listar-dizimo")
            return redirect("/dashboard/pages/listar-dizimo")

    @login_required(login_url="/dashboard/login/")
    def add_oferta(req):
        if req.method == 'POST':
            nome = req.POST.get('nome')
            cpf = req.POST.get('cpf')
            tel = req.POST.get('tel')
            valor = req.POST.get('value')
            token = req.POST.get('csrfmiddlewaretoken')

            if not token: 
                return HttpResponse({
                    "err":"Não existe token"
                })
            if cpf and valor:
                if nome and tel: 
                    if len(nome) < 4:
                            return JsonResponse({
                            "err":"Tamanho do nome oferta muito pequena"
                        },safe=False)
                    else:
                        Oferta.objects.create(name=nome,cpf=cpf,tel=tel,value=valor)
                        return JsonResponse({
                            "sucess":"adicionado com sucesso com sucesso"
                        },safe=False)
                else:
                    return JsonResponse({
                        "err":"Está faltando nome ou telefone"
                    },safe=False)
            else:
                return JsonResponse({
                    "err":"Está faltando cpf ou valor"
                },safe=False)

    @login_required(login_url="/dashboard/login/")
    def EditarOferta(req):
        if req.method == 'POST':
            print(req.POST)
            nome = req.POST.get('nome')
            cpf = req.POST.get('cpf')
            tel = req.POST.get('tel')
            valor = req.POST.get('value')
            id = req.POST.get('id')
            token = req.POST.get('csrfmiddlewaretoken')

            if not token: 
                return HttpResponse({
                    "err":"Não existe token"
                })
            if cpf and valor:
                if nome and tel: 
                    if len(nome) < 4:
                            return JsonResponse({
                            "err":"Tamanho do nome oferta muito pequena"
                        },safe=False)
                    else:
                        Oferta.objects.filter(id=id).update(name=nome,cpf=cpf,tel=tel,value=valor)
                        return JsonResponse({
                            "sucess":"Editado com sucesso com sucesso"
                        },safe=False)
                else:
                    return JsonResponse({
                        "err":"Está faltando nome ou telefone"
                    },safe=False)
            else:
                return JsonResponse({
                    "err":"Está faltando cpf ou valor"
                },safe=False) 

    @login_required(login_url="/dashboard/login/")
    def deletar_oferta(req,id):
        if req.method == "GET":
            
            if id != 0:
                Oferta.objects.filter(id=id).delete()
                return redirect("/dashboard/pages/listar-oferta")
            return redirect("/dashboard/pages/listar-oferta")

    @login_required(login_url="/dashboard/login/")
    def deletar_post(req,id):
        if req.method == "GET":
            
            if id != 0:
                Post.objects.filter(id=id).delete()
                return redirect("/dashboard/pages/listar-post")
            return redirect("/dashboard/pages/listar-post")
                