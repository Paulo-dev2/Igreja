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
            user = req.user
            admin = user.is_staff
            context = {'username':user,"admin":admin}
            html_template = loader.get_template('home/agenda/' + "add-agenda" + ".html")
            return HttpResponse(html_template.render(context, req))


    @login_required(login_url="/dashboard/login/")
    def listaAgenda(req):
        if req.method == 'GET':
            user = req.user
            admin = user.is_staff
            agenda = Agenda.objects.all()
            context = {
                'agenda': agenda,
                'username':user,
                'admin': admin
            }

            return render(req,'home/agenda/listar-agenda.html',context)

    @login_required(login_url="/dashboard/login/")
    def editarAgenda(req,id):
        if req.method == 'GET':
            if id != 0:
                user = req.user
                admin = user.is_staff
                try:
                    dados = {'username':user,'admin':admin}
                    dados['agenda'] = Agenda.objects.get(id=id)
                    return render(req,'home/agenda/editar-agenda.html',dados)
                except Agenda.DoesNotExist:
                    return redirect("/dashboard/pages/listar-agenda/")


    @login_required(login_url="/dashboard/login/")
    def addDizimo(req):
        if req.method == 'GET':
            user = req.user
            admin = user.is_staff
            context = {'username':user,'admin':admin}
            html_template = loader.get_template('home/dizimo/' + "add-dizimo" + ".html")
            return HttpResponse(html_template.render(context, req))

    @login_required(login_url="/dashboard/login/")
    def listarDizimo(req):
        if req.method == 'GET':
            user = req.user
            admin = user.is_staff
            dizimo = Dizimo.objects.all()
            context = {
                'dizimo': dizimo,
                'username':user,
                'admin':admin
            }

            return render(req,'home/dizimo/listar-dizimo.html',context)

    @login_required(login_url="/dashboard/login/")
    def editarDizimo(req,id):
        if req.method == 'GET':
            if id != 0:
                user = req.user
                admin = user.is_staff
                try:
                    dados = {'username':user,'admin':admin}
                    dados['dizimo'] = Dizimo.objects.get(id=id)
                    return render(req,'home/dizimo/editar-dizimo.html',dados)
                except Dizimo.DoesNotExist:
                    return redirect("/dashboard/pages/listar-dizimo/")

    @login_required(login_url="/dashboard/login/")
    def addOferta(req):
        if req.method == 'GET':
            user = req.user
            admin = user.is_staff
            context = {'username':user,'admin':admin}
            html_template = loader.get_template('home/oferta/' + "add-oferta" + ".html")
            return HttpResponse(html_template.render(context, req))

    @login_required(login_url="/dashboard/login/")
    def listarOferta(req):
        if req.method == 'GET':
            oferta = Oferta.objects.all()
            user = req.user
            admin = user.is_staff
            context = {
                'oferta': oferta,
                'username':user,
                'admin':admin
            }

            return render(req,'home/oferta/listar-oferta.html',context)

    @login_required(login_url="/dashboard/login/")
    def editarOferta(req,id):
        if req.method == 'GET':
            if id != 0:
                user = req.user
                admin = user.is_staff
                try:
                    dados = {'username':user,'admin':admin}
                    dados['oferta'] = Oferta.objects.get(id=id)
                    return render(req,'home/oferta/editar-oferta.html',dados)
                except Oferta.DoesNotExist:
                    return redirect("/dashboard/pages/listar-oferta/")

    @login_required(login_url="/dashboard/login/")
    def addPost(req):
        if req.method == 'POST':
            form = PostForm(req.POST)
            user = req.user
            admin = user.is_staff
            context = {'form':form,'username':user,'admin':admin}
           
        else:
            form = PostForm()
            user = req.user
            context = {'form':form,'username':user}
        html_template = loader.get_template('home/post/' + "add-post" + ".html")
        return HttpResponse(html_template.render(context, req))

    @login_required(login_url="/dashboard/login/")
    def addPostData(req):
        if req.method == 'POST':
            id = req.POST.get('id') if req.POST.get('id') else None
            title = req.POST.get('title') if req.POST.get('title') else None
            img = req.FILES.get('image') if req.FILES.get('image') else None
            text = req.POST.get('text') if req.POST.get('text') else None
            resumo = req.POST.get('resumo') if req.POST.get('resumo') else None
            user = req.user
            token = req.POST.get('csrfmiddlewaretoken') if req.POST.get('csrfmiddlewaretoken') else None
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
            user = req.user
            admin = user.is_staff
            post = Post.objects.all()
            context = {
                'post': post,
                'media_root': MEDIA_ROOT,
                'media_url': MEDIA_URL,
                'username':user,
                'admin':admin
            }
            return render(req,'home/post/listar-post.html',context)
        
    @login_required(login_url="/dashboard/login/")
    def DetailPost(req,id):
        if req.method == 'GET':
            user = req.user
            admin = user.is_staff
            dados = {'username':user,'admin':admin}
            dados['post'] = Post.objects.get(id=id)
            return render(req,'home/post/details-post.html',dados)

    @login_required(login_url="/dashboard/login/")
    def editarPost(req,id):
        if req.method == 'GET':
            if id != 0:
                user = req.user
                admin = user.is_staff
                try:
                    item = Post.objects.get(id=id)
                    dados = {'username':user,'admin':admin}
                    dados['post'] = item
                    dados['form'] = PostForm(instance=item)
                    return render(req,'home/post/editar-post.html',dados)
                except Post.DoesNotExist:
                    return redirect("/dashboard/pages/listar-post")

    @login_required(login_url="/dashboard/login/")
    def addEventos(req):
        if req.method == 'GET':
            user = req.user
            admin = user.is_staff
            context = {'username':user,'admin':admin}
            return render(req,"home/eventos/add-evento.html",context)

    @login_required(login_url="/dashboard/login/")
    def addEvento(req):
        if req.method == "POST":
            id = req.POST.get('id') if req.POST.get('id') else None
            nome = req.POST.get('nome') if req.POST.get('nome') else None
            vinculo = req.POST.get('vinculo') if req.POST.get('vinculo') else None
            Dt_start = req.POST.get('data_evento_start') if req.POST.get('data_evento_start') else None
            Dt_end = req.POST.get('data_evento_end') if req.POST.get('data_evento_end') else None
            img = req.FILES.get('image') if req.FILES.get('image') else None

            if id == None:
                if Sistema.reduzir_ifs(name = nome,vincule = vinculo,image = img,dt_inicio = Dt_start,dt_end = Dt_end):
                    Evento.objects.create(name=nome,image=img,vinculo = vinculo,data_start=Dt_start,data_end=Dt_end)
                    messages.success(req, "Evento criado Atualizado com sucesso")
                    return redirect("/dashboard/pages/listar-evento/")
                
                else:

                    messages.error(req,"Têm campos faltando coms os valores")
                    return redirect("/dashboard/pages/add-evento/")
            else:
                if Sistema.reduzir_ifs(id = id,name = nome,vinculo = vinculo,dt_inicio = Dt_start,dt_end = Dt_end):
                    obj = Evento.objects.get(id=id)
                    obj.name = nome
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
                user = req.user
                admin = user.is_staff
                try:
                    dados = {'username':user,'admin':admin}
                    dados['evento'] = Evento.objects.get(id=id)
                    return render(req,'home/eventos/editar-evento.html',dados)
                except Evento.DoesNotExist:
                    return redirect("/dashboard/pages/listar-evento")

    @login_required(login_url="/dashboard/login/")
    def ListarEvento(req):
        evento = Evento.objects.all()
        user = req.user
        admin = user.is_staff
        context = {
            'evento': evento,
            'media_root': MEDIA_ROOT,
            'media_url': MEDIA_URL,
            'username':user,
            'admin':admin
        }
        return render(req,'home/eventos/listar-evento.html',context)

    @login_required(login_url="/dashboard/login/")
    def ListaFeedback(req):
        if req.method == 'GET':
            feedback = Contato.objects.all()
            user = req.user
            admin = user.is_staff
            context = {
                'feedback': feedback,
                'username':user,
                'admin':admin
            }
            return render(req,'home/feedback/listar-feedback.html',context)

    @login_required(login_url="/dashboard/login/")
    def DetailsFeedback(req,id):
        if req.method == 'GET':
            try:
                feedback = Contato.objects.get(id=id)
                user = req.user
                admin = user.is_staff
                context = {
                    'feedback': feedback,
                    'username':user,
                    'admin':admin
                }
                return render(req,'home/feedback/details-feedback.html',context)
            except Contato.DoesNotExist:
                return redirect("/dashboard/pages/listar-feedback")

    @login_required(login_url="/dashboard/login/")
    def addSlide(req):
        if req.method == 'GET':
            user = req.user
            admin = user.is_staff
            context = {'username':user,'admin':admin}
            return render(req,"home/slides/add-slide.html",context)

    @login_required(login_url="/dashboard/login/")
    def addSlideData(req):
        if req.method == 'POST':
            id = req.POST.get('id') if req.POST.get('id') else None
            caption1 = req.POST.get('caption1') if req.POST.get('caption1') else None
            caption2 = req.POST.get('caption2') if req.POST.get('caption2') else None
            ativo = req.POST.get('status') if req.POST.get('status') else None
            img = req.FILES.get('image') if req.FILES.get('image') else None
            token = req.POST.get('csrfmiddlewaretoken') if req.POST.get('csrfmiddlewaretoken') else None
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
        user = req.user
        admin = user.is_staff
        context = {
            'slide': slide,
            'media_root': MEDIA_ROOT,
            'media_url': MEDIA_URL,
            'username':user,
            'admin':admin
        }
        return render(req,'home/slides/listar-slide.html',context)

    @login_required(login_url="/dashboard/login/")
    def editarSlide(req,id):
        if req.method == 'GET':
            if id != 0:
                user = req.user
                admin = user.is_staff
                try:
                    dados = {'username':user,'admin':admin}
                    dados['slide'] = Slide.objects.get(id=id)
                    return render(req,'home/slides/editar-slide.html',dados)
                except Slide.DoesNotExist:
                    return redirect('/dashboard/pages/listar-slide/')
    
    def login(req):
        if req.method == 'GET':
            return render(req,'admin/login.html')
    
    @login_required(login_url="/dashboard/login/")
    def addUserData(req):
        msg = None
        success = False
        user = req.user
        admin = user.is_staff

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

        return render(req, "home/user/add-user.html", {"form": form, "msg": msg, "success": success,'username':user,'admin':admin})

    @login_required(login_url="/dashboard/login/")
    def ListarUser(req):
        if req.method == 'GET':
            username = req.user
            admin = username.is_staff
            User = get_user_model()
            users = User.objects.all()
            return render(req, "home/user/listar-user.html", {"users":users,'username':username,'admin':admin})

    @login_required(login_url="/dashboard/login/")
    def EditarUser(req,id):
        if req.method == 'GET':
            username = req.user
            try:
                User = get_user_model()
                user = User.objects.get(id=id)
                return render(req, "home/user/editar-user.html", {"user":user,"username":username})
            except User.DoesNotExist:
                return redirect("/dashboard/pages/listar-user")

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

    @login_required(login_url="/dashboard/login/")
    def Profile(req):
        if req.method == 'GET':
            user = req.user
            id = user.id
            admin = user.is_staff
            User = get_user_model()
            users = User.objects.get(id=id)
            context = {'username':user,'admin':admin,'profile':users}
            return render(req,"home/profile/details-profile.html",context)

    @login_required(login_url="/dashboard/login/")
    def ProfileData(req):
        if req.method == 'POST':
            user = req.user
            admin = user.is_staff

            id = req.POST.get('id') if req.POST.get('id') else None
            first_name = req.POST.get('first_name') if req.POST.get('first_name') else None
            last_name = req.POST.get('last_name') if req.POST.get('last_name') else None
            username = req.POST.get('username') if req.POST.get('username') else None
            email = req.POST.get('email') if req.POST.get('email') else None

            if Sistema.reduzir_ifs(id=id, first_name=first_name, last_name=last_name, username=username,email=email):

                User = get_user_model()
                users = User.objects.get(id=id)
                users.username = username
                users.email = email
                users.first_name = first_name
                users.last_name = last_name
                users.save()
                print(first_name + ' ' + last_name)
                return redirect("/dashboard/pages/profile")
            else:
               return redirect("/dashboard/pages/profile") 