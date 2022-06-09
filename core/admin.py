from django.contrib import admin
from core.models import *

admin.site.login_template = 'admin/accounts/login.html'


class AgendaAdmin(admin.ModelAdmin):
    list_display = ('name','data_start')

class EventosAdmin(admin.ModelAdmin):
    list_display = ('name','data_start','data_end')

class SlideAdmin(admin.ModelAdmin):
    list_display = ('caption1','caption2','image','is_active')

class DizimoAdmin(admin.ModelAdmin):
    lista_display = ('name','cpf','tel','value','data')

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('name','cpf','tel','value','data')

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_date','title','image')

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('name_from','email_from')

class EmailAdmin(admin.ModelAdmin):
    list_display = ('title','email_to')


admin.site.register(Agenda,AgendaAdmin)
admin.site.register(Evento,EventosAdmin)
admin.site.register(Slide,SlideAdmin)
admin.site.register(Dizimo,DizimoAdmin)
admin.site.register(Oferta,OfertaAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Contato,ContatoAdmin)
admin.site.register(Email,EmailAdmin)
admin.site.register(Igreja)