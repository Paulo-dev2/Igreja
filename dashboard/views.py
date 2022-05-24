from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required

class Dashboard:

    @login_required(login_url="login/")
    def add_agendas(request):
        redirect("/dashboard")
        return HttpResponse("Olá mundo")


""" except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request)) """