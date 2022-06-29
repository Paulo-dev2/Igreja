from django.shortcuts import render,redirect
from core.models import Agenda,Slide,Evento,Post,Contato
from sys_igreja.settings import MEDIA_URL
from dashboard.forms import PostForm
from dashboard.metodos.system import Sistema
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.utils import timezone

def Erro404(req,exception):
    return render(req, 'home/page-404.html')

class User:
    def home(req):
        if req.method == 'GET':
            slide = Slide.objects.all()
            horaAtual = datetime.now(tz=timezone.utc)
            agendas = Agenda.objects.all().filter(data_start__gt=horaAtual)
            eventos = Evento.objects.all().filter(data_end__gt=horaAtual)
            context = {'slides': slide,'agendas':agendas,'eventos': eventos,'media_url': MEDIA_URL}
            return render(req, 'user/home.html',context)

    def agendas(req):
        if req.method == 'GET':
            horaAtual = datetime.now(tz=timezone.utc)
            agendas = Agenda.objects.all().filter(data_start__gt=horaAtual)
            context = {'agendas':agendas}
            return render(req, 'user/agenda.html',context)

    def eventos(req):
        if req.method == 'GET':
            horaAtual = datetime.now(tz=timezone.utc)
            eventos = Evento.objects.all().filter(data_end__gt=horaAtual)
            context = {'eventos': eventos,'media_url': MEDIA_URL}
            return render(req, 'user/evento.html',context)

    def blog(req):
        if req.method == 'GET':
            posts = Post.objects.all()
            context = {'posts':posts,'media_url': MEDIA_URL}
            return render(req, 'user/blog.html',context)

    def blog_detail(req,id):
        if req.method == 'GET':
            if id != 0:
                try:
                    item = Post.objects.get(id=id)
                    dados = {}
                    dados['post'] = item
                    dados['form'] = PostForm(instance=item)
                    dados['media_url'] = MEDIA_URL
                    return render(req,'user/blog-detail.html',dados)
                except Post.DoesNotExist:
                    return redirect("/blog")

    def contato(req):
        if req.method == 'GET':
            context = {'messages': messages.get_messages(req)}
            return render(req, 'user/contato.html',context)

    def contatoSubmit(req):
        if req.method == 'POST':
            nome = req.POST.get('name') if req.POST.get('name') else None
            email = req.POST.get('email') if req.POST.get('email') else None
            tel = req.POST.get('phone') if req.POST.get('phone') else None
            message = req.POST.get('message') if req.POST.get('message') else None

            if Sistema.reduzir_ifs(nome=nome,email=email,tel=tel,message=message):
                Contato.objects.create(name_from=nome,email_from=email,telefone=tel,text_from=message)
                msg = "Mensagem enviada com sucesso"
                type = "sucess"
            else:
                msg = "Mensagem não enviada"
                type = "error"

            context = {'mensagens': msg,'type': type}
            return render(req, 'user/contato.html',context)

    def sobreNos(req):
        if req.method == 'GET':
            slide = Slide.objects.all()
            agendas = Agenda.objects.all()
            eventos = Evento.objects.all()
            context = {'slides': slide,'agendas':agendas,'eventos': eventos,'media_url': MEDIA_URL}
            return render(req, 'user/about.html',context)
