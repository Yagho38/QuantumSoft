from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import *

AdminSite.site_header = 'Administração QuantumSoft'
AdminSite.site_title = 'Administração QuantumSoft'
AdminSite.index_title = 'Administração QuantumSoft'


@admin.register(Leads)
class Leads(admin.ModelAdmin):
	list_display = ('nome', 'email', 'telefone', 'criado')

@admin.register(Contato)
class Contato(admin.ModelAdmin):
	list_display = ('nome', 'email', 'assunto', 'mensagem', 'criado')