from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from core.models import Agenda,Evento,Dizimo,Oferta,Contato,Slide
from dashboard.forms import PostForm,SignUpForm
from django.contrib import messages
from sys_igreja.settings import MEDIA_ROOT, MEDIA_URL
from core.models import Post
from dashboard.metodos.system import Sistema
from django.contrib.auth import authenticate, get_user_model

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
        id = req.POST.get('id') if req.POST.get('id') else None
        title = req.POST.get('title') if req.POST.get('title') else None
        img = req.FILES.get('image') if req.FILES.get('image') else None
        text = req.POST.get('text') if req.POST.get('text') else None
        resumo = req.POST.get('resumo') if req.POST.get('resumo') else None
        user = req.user
        token = req.POST.get('csrfmiddlewaretoken') if req.POST.get('csrfmiddlewaretoken') else None

        if req.method == 'POST':
            if token != None:
                if id != None:
                    if Sistema.reduzir_ifs(titulo=title,resumo=resumo):
                        obj = Post.objects.get(id=id)
                        obj.title = title
                        obj.text = text
                        obj.resumo = resumo
                        obj.save()
                        #Post.objects.filter(id=id).update(title=title,author=user,image=img,text=text)
                        messages.success(req, "Post Atualizado com sucesso")
                        return redirect("/dashboard/pages/listar-post/")
                      
                else:
                    if Sistema.reduzir_ifs(image=img, titulo=title, resumo=resumo):
                        Post.objects.create(title=title,author=user,image=img,text=text,resumo=resumo)
                        messages.success(req, "Post Criado com sucesso")
                        return redirect("/dashboard/pages/listar-post/")
                                
                    else:
                        messages.success(req, "Tem campos vazios")
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

    @login_required(login_url="/dashboard/login/")
    def addEventos(req):
        if req.method == 'GET':
            context = {}
            return render(req,"home/eventos/add-evento.html",context)

    @login_required(login_url="/dashboard/login/")
    def addEvento(req):
        id = req.POST.get('id') if req.POST.get('id') else None
        nome = req.POST.get('nome') if req.POST.get('nome') else None
        qtd = req.POST.get('qtd_ingresso') if req.POST.get('qtd_ingresso') else None
        preco = req.POST.get('preco') if req.POST.get('preco') else None
        valor_temporario = str(preco.replace('.','').replace(',',''))
        valor_completo = valor_temporario[:-2]
        preco = float(valor_completo)
        vinculo = req.POST.get('vinculo') if req.POST.get('vinculo') else None
        Dt_start = req.POST.get('data_evento_start') if req.POST.get('data_evento_start') else None
        Dt_end = req.POST.get('data_evento_end') if req.POST.get('data_evento_end') else None
        img = req.FILES.get('image') if req.FILES.get('image') else None

        if id == None:
            if Sistema.reduzir_ifs(name = nome,quantidade = qtd,price = preco,vincule = vinculo,image = img,dt_inicio = Dt_start,dt_end = Dt_end):
                Evento.objects.create(name=nome,image=img,quantidade_ingressos=qtd,preco=preco,vinculo = vinculo,data_start=Dt_start,data_end=Dt_end)
                messages.success(req, "Evento criado Atualizado com sucesso")
                return redirect("/dashboard/pages/listar-evento/")
            
            else:

                messages.error(req,"Têm campos faltando coms os valores")
                return redirect("/dashboard/pages/add-evento/")
        else:
            if Sistema.reduzir_ifs(id = id,name = nome,quantidade_ingressos = qtd,preco = preco,vinculo = vinculo,dt_inicio = Dt_start,dt_end = Dt_end):
                obj = Evento.objects.get(id=id)
                obj.name = nome
                obj.quantidade_ingressos = qtd
                obj.preco = preco
                obj.vinculo = vinculo
                obj.dt_inicio = Dt_start
                obj.dt_end = Dt_end 
                obj.save()
                messages.success(req, "Evento Atualizado com sucesso")
                return redirect("/dashboard/pages/listar-evento/")
            else:
                messages.error(req,"Têm campos faltando coms os valores")
                return redirect(f"/dashboard/pages/editar-evento/{id}")

    @login_required(login_url="/dashboard/login/")
    def editarEvento(req,id):
        if req.method == 'GET':
            if id != 0:
                dados = {}
                dados['evento'] = Evento.objects.get(id=id)
                return render(req,'home/eventos/editar-evento.html',dados)

    @login_required(login_url="/dashboard/login/")
    def ListarEvento(req):
        evento = Evento.objects.all()
        context = {
            'evento': evento,
            'media_root': MEDIA_ROOT,
            'media_url': MEDIA_URL
        }
        return render(req,'home/eventos/listar-evento.html',context)

    @login_required(login_url="/dashboard/login/")
    def ListaFeedback(req):
        feedback = Contato.objects.all()
        context = {
            'feedback': feedback
        }
        return render(req,'home/feedback/listar-feedback.html',context)

    @login_required(login_url="/dashboard/login/")
    def addSlide(req):
        if req.method == 'GET':
            context = {}
            return render(req,"home/slides/add-slide.html",context)

    @login_required(login_url="/dashboard/login/")
    def addSlideData(req):
        id = req.POST.get('id') if req.POST.get('id') else None
        caption1 = req.POST.get('caption1') if req.POST.get('caption1') else None
        caption2 = req.POST.get('caption2') if req.POST.get('caption2') else None
        ativo = req.POST.get('status') if req.POST.get('status') else None
        img = req.FILES.get('image') if req.FILES.get('image') else None
        token = req.POST.get('csrfmiddlewaretoken') if req.POST.get('csrfmiddlewaretoken') else None

        if req.method == 'POST':
            if token is not None:
                if id is None:
                    if Sistema.reduzir_ifs(caption1=caption1,caption2=caption2,ativo=ativo,img=img):
                        Slide.objects.create(caption1=caption1,caption2=caption2,is_active=ativo,image=img)
                        messages.success(req,"Slide Criado com sucesso")
                        return redirect('/dashboard/pages/listar-slide/')
                else: 
                    if Sistema.reduzir_ifs(caption1=caption1,caption2=caption2,ativo=ativo):
                        obj = Slide.objects.get(id=id)
                        obj.caption1 = caption1
                        obj.caption2 = caption2
                        obj.is_active = ativo
                        obj.save()
                        messages.success(req,"Slide Editado com sucesso")
                        return redirect('/dashboard/pages/listar-slide/')
                    else: 
                        print(req.FILES.get('image'))
                        return redirect('/dashboard/pages/listar-slide/')
            else:
                return redirect('/dashboard/pages/listar-slide/')
        else:
            return redirect('/dashboard/pages/listar-slide/')

    @login_required(login_url="/dashboard/login/")
    def ListaSlides(req):
        slide = Slide.objects.all()
        context = {
            'slide': slide,
            'media_root': MEDIA_ROOT,
            'media_url': MEDIA_URL
        }
        return render(req,'home/slides/listar-slide.html',context)

    @login_required(login_url="/dashboard/login/")
    def editarSlide(req,id):
        if req.method == 'GET':
            if id != 0:
                dados = {}
                dados['slide'] = Slide.objects.get(id=id)
                return render(req,'home/slides/editar-slide.html',dados)
    
    def login(req):
        if req.method == 'GET':
            return render(req,'admin/login.html')
    
    @login_required(login_url="/dashboard/login/")
    def addUserData(req):
        msg = None
        success = False

        if req.method == "POST":
            form = SignUpForm(req.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=username, password=raw_password)

                msg = 'Usuario criado'
                success = True

                return redirect("/dashboard/pages/listar-user/")

            else:
                msg = 'Erro nos dados do formulário'
        else:
            form = SignUpForm()

        return render(req, "home/user/add-user.html", {"form": form, "msg": msg, "success": success})

    @login_required(login_url="/dashboard/login/")
    def ListarUser(req):
        if req.method == 'GET':
            User = get_user_model()
            users = User.objects.all()
            return render(req, "home/user/listar-user.html", {"users":users})

    @login_required(login_url="/dashboard/login/")
    def EditarUser(req,id):
        if req.method == 'GET':
            User = get_user_model()
            user = User.objects.get(id=id)
            print(user)
            return render(req, "home/user/editar-user.html", {"user":user})

    @login_required(login_url="/dashboard/login/")
    def EditarUserData(req):
        if req.method == 'POST':
            User = get_user_model()
            users = User.objects.get(id=req.POST.get('id'))
            users.username = req.POST.get('username').replace(" ","")
            users.email = req.POST.get('email')
            users.save()
            messages.success(req,"User Editado com sucesso")
            return redirect('/dashboard/pages/listar-user/')