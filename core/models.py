from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from datetime import datetime

class Agenda(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    data_start = models.DateTimeField(verbose_name="Dia marcado")

    def __str__(self):
        return self.name    

    def get_data_agenda(self):
        return self.data_start.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_formatado(self):
        return self.data_start.strftime('%Y-%m-%dT%H:%M')
    
    def agenda_ativa(self):
        print(self.data_start.strftime('%d/%m/%Y %H:%M Hrs'))
        print(datetime.now().strftime('%d/%m/%Y %H:%M Hrs'))
        mes_now =  datetime.now().strftime('%d/%m/%Y %H:%M Hrs').split(" ")[0].split("/")[1]
        mes_start =  self.data_start.strftime('%d/%m/%Y %H:%M Hrs').split(" ")[0].split("/")[1]

        ano_now =  datetime.now().strftime('%d/%m/%Y %H:%M Hrs').split(" ")[0].split("/")[2]
        ano_start =  self.data_start.strftime('%d/%m/%Y %H:%M Hrs').split(" ")[0].split("/")[2]

        if ano_start == ano_now:
            if mes_start == mes_now:
                if self.data_start.strftime('%d/%m/%Y %H:%M Hrs') > datetime.now().strftime('%d/%m/%Y %H:%M Hrs'):
                    return True
            return False
        return False

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'eventos/',help_text="Size: 1920x570",blank=True)
    quantidade_ingressos = models.IntegerField(blank=True)
    preco = models.FloatField(blank=True,null=True)
    vinculo = models.CharField(max_length=70,blank=True)
    data_start = models.DateTimeField()
    data_end = models.DateTimeField()

    def __str__(self):
        return self.name

    def __data_now(self):
        return datetime.now().strftime('%d/%m/%Y %H:%M Hrs')
    def get_value_formatado(self):
        valorReal = f'{self.preco:_.2f}'
        valorReal = valorReal.replace('.',',').replace('_','.')
        return valorReal

    def get_data_start_evento(self):
        return self.data_start.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_end_evento(self):
        return self.data_end.strftime('%d/%m/%Y %H:%M Hrs')


    def get_data_formatado_inicio(self):
        return self.data_start.strftime('%Y-%m-%dT%H:%M')

    def get_data_formatado_fim(self):
        return self.data_end.strftime('%Y-%m-%dT%H:%M')

    def evento_ativo_hoje(self):
        now = datetime.now().strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0]
        hoje_end = self.data_end.strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0]
        hoje_start = self.data_start.strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0]
        if hoje_start  ==  now:
            if hoje_end == now:
                now = datetime.now().strftime('%d/%m/%Y %H:%M Hrs').split(' ')[1]
                hoje_horario_end = self.data_end.strftime('%d/%m/%Y %H:%M Hrs').split(' ')[1]
                if hoje_horario_end > now:
                    return True

    def evento_ativo_mes(self):
        now_mes = datetime.now().strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0].split('/')[1]
        now_ano = datetime.now().strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0].split('/')[2]
        now_dia = datetime.now().strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0].split('/')[0]
        mes_start = self.data_start.strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0].split('/')[1]
        ano_start = self.data_start.strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0].split('/')[2]
        dia_start = self.data_start.strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0].split('/')[0]
        dia_end = self.data_end.strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0].split('/')[0]

        if mes_start  ==  now_mes:
            if ano_start == now_ano:
                if dia_start >= now_dia or dia_end >= now_dia: return True
                else: return False
            else: return False
        else: return False



    def evento_ativo_ano(self):
        now_ano = datetime.now().strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0].split('/')[2]
        ano_start = self.data_start.strftime('%d/%m/%Y %H:%M Hrs').split(' ')[0].split('/')[2]    
        if ano_start == now_ano: return True
        else: return False

""" class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    setor = models.CharField(max_length=50)
    descrition = models.TextField()
    def __str__(self):
        return self.name """

class Slide(models.Model):
    caption1 = models.CharField(max_length=100)
    caption2 = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'slides/', help_text="Size: 1920x570",blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.caption1, self.caption2)

class Dizimo(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=120)
    cpf = models.CharField(max_length=15)
    tel = models.CharField(max_length=15)
    value = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_value_dizimo(self):
        return self.value

    def get_data_formatado(self):
        return self.data.strftime('%d/%m/%Y %H:%M Hrs')

    def get_value_formatado(self):
        valorReal = f'{self.value:_.2f}'
        valorReal = valorReal.replace('.',',').replace('_','.')
        return valorReal

class Oferta(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=120)
    cpf = models.CharField(max_length=15)
    tel = models.CharField(max_length=15)
    value = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_value_oferta(self):
        return self.value

    def get_data_formatado(self):
        return self.data.strftime('%d/%m/%Y %H:%M Hrs')

    def get_value_formatado(self):
        valorReal = f'{self.value:_.2f}'
        valorReal = valorReal.replace('.',',').replace('_','.')
        return valorReal

""" def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit*1024*1024*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit)) 
    ,validators=[validate_image]    
    """

class Post(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    resumo = models.TextField(blank=True,null=True)
    text = RichTextField(blank=True,null=True)
    image = models.ImageField(upload_to = 'posts/', help_text="Tamanho maximo 4MB",blank=True)
    post_date = models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.title

    def get_data_formatado(self):
        return self.post_date.strftime('%d/%m/%Y %H:%M Hrs')

class Contato(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name_from = models.CharField(max_length=120)
    email_from = models.CharField(max_length=120)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    text_from = models.TextField()
    def __str__(self):
        return self.name_from + self.email_from

class Email(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    title = models.CharField(max_length=120)
    email_to = models.ForeignKey(Contato, on_delete=models.CASCADE,null=True)
    text = models.TextField()
    def __str__(self):
        return self.title
class Igreja(models.Model):
    name = models.CharField(max_length=120)
    cnpj = models.CharField(max_length=16)
    uf = models.CharField(max_length=25)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=25)
    cidade = models.CharField(max_length=70)
    rua = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name