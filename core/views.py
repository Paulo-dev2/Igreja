from django.shortcuts import render,redirect
from core.models import Agenda,Slide,Evento,Post,Contato
from sys_igreja.settings import MEDIA_URL
from dashboard.forms import PostForm
from dashboard.metodos.system import Sistema
from django.contrib import messages

class User:
    def home(req):
        if req.method == 'GET':
            slide = Slide.objects.all()
            agendas = Agenda.objects.all()
            eventos = Evento.objects.all()
            context = {'slides': slide,'agendas':agendas,'eventos': eventos,'media_url': MEDIA_URL}
            return render(req, 'user/home.html',context)

    def agendas(req):
        if req.method == 'GET':
            agendas = Agenda.objects.all()
            context = {'agendas':agendas}
            return render(req, 'user/agenda.html',context)

    def eventos(req):
        if req.method == 'GET':
            eventos = Evento.objects.all()
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
                item = Post.objects.get(id=id)
                dados = {}
                dados['post'] = item
                dados['form'] = PostForm(instance=item)
                dados['media_url'] = MEDIA_URL
                return render(req,'user/blog-detail.html',dados)

    def contato(req):
        if req.method == 'GET':
            return render(req, 'user/contato.html')

    def contatoSubmit(req):
        if req.method == 'POST':
            nome = req.POST.get('name') if req.POST.get('name') else None
            email = req.POST.get('email') if req.POST.get('email') else None
            tel = req.POST.get('phone') if req.POST.get('phone') else None
            message = req.POST.get('message') if req.POST.get('message') else None

            if Sistema.reduzir_ifs(nome=nome,email=email,tel=tel,message=message):
                Contato.objects.create(name_from=nome,email_from=email,telefone=tel,text_from=message)
                messages.success(req,"Mensagem enviada com sucesso")
                return redirect("/contato")
            else:
                messages.error(req,"Mensagem não enviada")
                return redirect("/contato")

    def sobreNos(req):
        if req.method == 'GET':
            slide = Slide.objects.all()
            agendas = Agenda.objects.all()
            eventos = Evento.objects.all()
            context = {'slides': slide,'agendas':agendas,'eventos': eventos,'media_url': MEDIA_URL}
            return render(req, 'user/about.html',context)
