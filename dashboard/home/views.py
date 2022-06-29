from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Agenda,Evento,Dizimo,Oferta
from datetime import datetime

@login_required(login_url="/dashboard/login/")
def index(request):
    user = request.user
    admin = user.is_staff
    agenda = Agenda.objects.all()
    eventos = Evento.objects.all()
    dizimo = Dizimo.objects.all().values()
    oferta = Oferta.objects.all().values()
    soma_dizimo = 0
    soma_oferta = 0

    for i in range(len(dizimo)): soma_dizimo += dizimo[i]["value"]
    for i in range(len(oferta)): soma_oferta += oferta[i]["value"]

    soma_tudo = soma_dizimo + soma_oferta

    data_agora = str(
        datetime.now().strftime('%d/%m/%Y %H:%M Hrs')
    )

    data = oferta[0]['data'].strftime('%d/%m/%Y %H:%M Hrs')
    mes = data.split('/')[1] ==  data_agora.split('/')[1] 

    soma_hoje = 0
    soma_mes = 0
    soma_ano = 0

    for i in range(len(oferta)):
        data_oferta = oferta[i]['data'].strftime('%d/%m/%Y %H:%M Hrs')
        hoje = data_oferta.split(' ')[0] == data_agora.split(' ')[0]
        mes = data_oferta.split('/')[1] ==  data_agora.split('/')[1]
        data_ano = oferta[i]['data'].strftime('%d/%m/%Y').split("/")[2]
        data_ano_agora =  str(
            datetime.now().strftime('%d/%m/%Y')
        ).split('/')[2]


        ano = data_ano ==  data_ano_agora

        #data_entrada[i] = { 'mes':data_oferta.split(" ")[0].split('/')[1],'value':oferta[i]['value']}

        if hoje: soma_hoje += oferta[i]['value']

        if mes: soma_mes += oferta[i]['value']

        if ano: soma_ano += oferta[i]['value']

    for i in range(len(dizimo)):
        data_dizimo= dizimo[i]['data'].strftime('%d/%m/%Y %H:%M Hrs')

        hoje = data_dizimo.split(' ')[0] == data_agora.split(' ')[0]
        mes = data_dizimo.split('/')[1] ==  data_agora.split('/')[1]
        data_ano = dizimo[i]['data'].strftime('%d/%m/%Y').split("/")[2]
        data_ano_agora =  str(
            datetime.now().strftime('%d/%m/%Y')
        ).split('/')[2]

        ano = data_ano ==  data_ano_agora

        #data_entrada[len(data_entrada) + i] = { 'mes':data_oferta.split(" ")[0].split('/')[1],'value':oferta[i]['value']}

        if hoje: soma_hoje += dizimo[i]['value']

        if mes: soma_mes += dizimo[i]['value']

        if ano: soma_ano += dizimo[i]['value']


    valorRealHoje = f'{soma_hoje:_.2f}'
    valorRealHoje = valorRealHoje.replace('.',',').replace('_','.')
    
    valorRealMes = f'{soma_mes:_.2f}'
    valorRealMes = valorRealMes.replace('.',',').replace('_','.')

    valorRealAno = f'{soma_ano:_.2f}'
    valorRealAno = valorRealAno.replace('.',',').replace('_','.')
    context = {
        'segment':'index',
        'agenda': agenda,
        'eventos': eventos,
        'hoje':valorRealHoje,
        'mes':valorRealMes,
        'ano': valorRealAno,
        'username':user,
        'admin': admin,
        #'saida':data_entrada
    }
    return render(request,'home/index.html',context)

