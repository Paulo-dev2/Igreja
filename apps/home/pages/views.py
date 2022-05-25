from gc import get_objects
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from core.models import Agenda,Evento,Dizimo,Oferta
from apps.authentication.forms import PostForm
from django.contrib import messages
from sys_igreja.settings import MEDIA_ROOT, MEDIA_URL
from core.models import Post

class Pages:
    @login_required(login_url="/dashboard/login/")
    def addAgenda(req):
        if req.method == 'GET':
            context = {}
            html_template = loader.get_template('home/agenda/' + "add-agenda" + ".html")
            return HttpResponse(html_template.render(context, req))


    @login_required(login_url="/dashboard/login/")
    def listaAgenda(req):
        if req.method == 'GET':
            agenda = Agenda.objects.all()
            context = {
                'agenda': agenda,
            }

            return render(req,'home/agenda/listar-agenda.html',context)

    @login_required(login_url="/dashboard/login/")
    def editarAgenda(req,id):
        if req.method == 'GET':
            if id != 0:
                dados = {}
                dados['agenda'] = Agenda.objects.get(id=id)
                return render(req,'home/agenda/editar-agenda.html',dados)

    @login_required(login_url="/dashboard/login/")
    def addDizimo(req):
        if req.method == 'GET':
            context = {}
            html_template = loader.get_template('home/dizimo/' + "add-dizimo" + ".html")
            return HttpResponse(html_template.render(context, req))

    @login_required(login_url="/dashboard/login/")
    def listarDizimo(req):
        if req.method == 'GET':
            dizimo = Dizimo.objects.all()
            context = {
                'dizimo': dizimo,
            }

            return render(req,'home/dizimo/listar-dizimo.html',context)

    @login_required(login_url="/dashboard/login/")
    def editarDizimo(req,id):
        if req.method == 'GET':
            if id != 0:
                dados = {}
                dados['dizimo'] = Dizimo.objects.get(id=id)
                return render(req,'home/dizimo/editar-dizimo.html',dados)

    @login_required(login_url="/dashboard/login/")
    def addOferta(req):
        if req.method == 'GET':
            context = {}
            html_template = loader.get_template('home/oferta/' + "add-oferta" + ".html")
            return HttpResponse(html_template.render(context, req))

    @login_required(login_url="/dashboard/login/")
    def listarOferta(req):
        if req.method == 'GET':
            oferta = Oferta.objects.all()
            context = {
                'oferta': oferta,
            }

            return render(req,'home/oferta/listar-oferta.html',context)

    @login_required(login_url="/dashboard/login/")
    def editarOferta(req,id):
        if req.method == 'GET':
            if id != 0:
                dados = {}
                dados['oferta'] = Oferta.objects.get(id=id)
                return render(req,'home/oferta/editar-oferta.html',dados)

    @login_required(login_url="/dashboard/login/")
    def addPost(req):
        if req.method == 'POST':
            form = PostForm(req.POST)
            context = {'form':form}
           
        else:
            form = PostForm()
            context = {'form':form}
        html_template = loader.get_template('home/post/' + "add-post" + ".html")
        return HttpResponse(html_template.render(context, req))

    @login_required(login_url="/dashboard/login/")
    def addPostData(req):
        id = req.POST.get('id')
        title = req.POST.get('title')
        img = req.FILES.get('image')
        text = req.POST.get('text')
        user = req.user


        if req.method == 'POST':
            if id:
                if img:
                    if title:
                        if text:
                            if req.POST.get('csrfmiddlewaretoken'):
                                obj = Post.objects.get(id=id)
                                obj.image = img
                                obj.title = title
                                obj.text = text
                                obj.save()
                                #Post.objects.filter(id=id).update(title=title,author=user,image=img,text=text)
                                messages.success(req, "Produto Atualizado com sucesso")
                                return redirect("/dashboard/pages/listar-post/")
                        else:
                            messages.success(req, "Erro no text")
                            return redirect("/dashboard/pages/edit-post/")
                    else:
                        messages.success(req, "É obrigado a ter titulo!!")
                        return redirect("/dashboard/pages/edit-post/")
                else:
                    messages.success(req, "É obrigado a ter imagem!!")
                    return redirect(f"/dashboard/pages/editar-post/{id}")
            else:
                if img:
                    if title:
                        if text:
                            if req.POST.get('csrfmiddlewaretoken'):
                                Post.objects.create(title=title,author=user,image=img,text=text)
                                return redirect("/dashboard/pages/listar-post/")
                        else:
                            messages.success(req, "Erro no text")
                            return redirect("/dashboard/pages/edit-post/")
                    else:
                        messages.success(req, "É obrigado a ter titulo!!")
                        return redirect("/dashboard/pages/edit-post/")
                else:
                    messages.success(req, "É obrigado a ter imagem!!")
                    return redirect(f"/dashboard/pages/editar-post/{id}")

    @login_required(login_url="/dashboard/login/")
    def ListarPost(req):
        if req.method == 'GET':
            post = Post.objects.all()
            context = {
                'post': post,
                'media_root': MEDIA_ROOT,
                'media_url': MEDIA_URL
            }
            return render(req,'home/post/listar-post.html',context)
        
    @login_required(login_url="/dashboard/login/")
    def DetailPost(req,id):
        if req.method == 'GET':
            dados = {}
            dados['post'] = Post.objects.get(id=id)
            return render(req,'home/post/details-post.html',dados)

    @login_required(login_url="/dashboard/login/")
    def editarPost(req,id):
        if req.method == 'GET':
            if id != 0:
                item = Post.objects.get(id=id)
                dados = {}
                dados['post'] = item
                dados['form'] = PostForm(instance=item)
                print(dados['post'])
                return render(req,'home/post/editar-post.html',dados)

    def login(req):
        if req.method == 'GET':
            return render(req,'home/login.html')

""" @login_required(login_url="login/")
def pages(request):
    if request.method == 'GET':
        context = {}
        # All resource paths end in .html.
        # Pick out the html file name from the url. And load that template.
        try:

            load_template = request.path.split('/')[-1]

            if load_template == 'admin':
                return HttpResponseRedirect(reverse('admin:index'))
            context['segment'] = load_template

            dir = load_template.split("-")[1]

            html_template = loader.get_template('home/' + dir + '/' + load_template + ".html")
            return HttpResponse(html_template.render(context, request))

        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/page-404.html')
            return HttpResponse(html_template.render(context, request))

        except:
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request)) """