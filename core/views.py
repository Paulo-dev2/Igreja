from django.shortcuts import render,HttpResponse,redirect
from core.models import Agenda
from django.contrib.auth.decorators import login_required

""" return redirect('/hello') """

@login_required()
def hello(req):
    agenda = Agenda.objects.all()
    response = {'agenda': agenda}
    return render(req, 'teste.html',response)
