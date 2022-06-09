# -*- encoding: utf-8 -*-
from django.http import JsonResponse
import os
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Agenda,Evento,Dizimo,Oferta,Post,Contato, Slide
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from sys_igreja.settings import MEDIA_ROOT
from dashboard.metodos.system import Sistema
from django.contrib.auth import authenticate, get_user_model
from django.contrib import messages

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
            valor_temporario = str(req.POST.get('value').replace('.','').replace(',',''))
            valor_completo = valor_temporario[:-2]
            valor = float(valor_completo)
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
            valor_temporario = str(req.POST.get('value').replace('.','').replace(',',''))
            valor_completo = valor_temporario[:-2]
            valor = float(valor_completo)
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
            valor_temporario = str(req.POST.get('value').replace('.','').replace(',',''))
            valor_completo = valor_temporario[:-2]
            valor = float(valor_completo)
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
            valor_temporario = str(req.POST.get('value').replace('.','').replace(',',''))
            valor_completo = valor_temporario[:-2]
            valor = float(valor_completo)
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
                delete = Post.objects.filter(id=id).values()
                image_delete = MEDIA_ROOT.replace("\\",'/') +  delete[0]['image']
                Sistema.Delete_Image(image_delete)
                Post.objects.filter(id=id).delete()
                return redirect("/dashboard/pages/listar-post")
            return redirect("/dashboard/pages/listar-post")
            
    @login_required(login_url="/dashboard/login/")
    def deletar_evento(req,id):
        if req.method == "GET":
            
            if id != 0:
                delete = Evento.objects.filter(id=id).values()
                image_delete = MEDIA_ROOT.replace("\\",'/') +  delete[0]['image']
                Sistema.Delete_Image(image_delete)
                Evento.objects.filter(id=id).delete()
                return redirect("/dashboard/pages/listar-evento")
            return redirect("/dashboard/pages/listar-evento")

    @login_required(login_url="/dashboard/login/")
    def deletar_feedback(req,id):
        if req.method == "GET":
            
            if id != 0:
                Contato.objects.filter(id=id).delete()
                return redirect("/dashboard/pages/listar-feedback")
            return redirect("/dashboard/pages/listar-feedback")          

    @login_required(login_url="/dashboard/login/")
    def deletar_slide(req,id):
        if req.method == "GET":
            
            if id != 0:
                delete = Slide.objects.filter(id=id).values()
                image_delete = MEDIA_ROOT.replace("\\",'/') +  delete[0]['image']
                Sistema.Delete_Image(image_delete)
                Slide.objects.filter(id=id).delete()
                return redirect("/dashboard/pages/listar-slide")
            return redirect("/dashboard/pages/listar-slide")      

    @login_required(login_url="/dashboard/login/")
    def DeleteUser(req,id):
        if req.method == 'GET':
            User = get_user_model()
            User.objects.filter(id=id).delete()
            messages.success(req,"Deletado com sucesso")
            return redirect("/dashboard/pages/listar-user/") 

#one_piece_fD3AYxe.jpg