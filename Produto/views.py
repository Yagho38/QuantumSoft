from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render
from django.db.models import F, Q
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
from django import forms
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import update_session_auth_hash
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views import generic, View
from random import randint
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
import json
import time

def home(request):
	if str(request.method) == 'POST':
		form1 = FormContato(request.POST)
		form2 = FormLeads(request.POST)
		if form1.is_valid():
			form1.save()
			messages.success(request, 'Contato enviado com sucesso!')
		elif form2.is_valid():
			form2.save()
			messages.success(request, 'Sucesso! Em Breve Entraremos em Contato!')
		else:
			messages.error(request, 'Por favor revise seu formulário, algo deu errado!')
	else:
		form1 = FormContato()
		form2 = FormLeads()
	return render(request, 'index.html', {'form1': form1, 'form2': form2})
	

#def recuperarSenha(request):
#	return render(request, 'registration/recuperarSenha.html')