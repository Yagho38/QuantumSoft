from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.mail.message import EmailMessage
from django.http import HttpResponse
from django.views import generic


class FormContato(forms.ModelForm):
	class Meta:
		model = Contato
		fields = ['nome', 'email', 'assunto', 'mensagem']

class FormLeads(forms.ModelForm):
	class Meta:
		model = Leads
		fields = ['nome', 'email', 'telefone']