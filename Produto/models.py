from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
import uuid

def get_file_path(instance,filename):
	ext = filename.split('.')[-1]
	filename = f'{uuid.uuid4()}.{ext}'
	return filename

class Base(models.Model):
	criado = models.DateField('Data de criacao', auto_now_add=True)
	modificado = models.DateField('Data da ultima modificacao', auto_now=True)
	ativo = models.BooleanField('Ativo?', default=True)
	class Meta:
		abstract = True

class Leads(Base):
	nome = models.CharField('Nome', max_length=100)
	email = models.EmailField('Email')
	telefone = models.CharField('Telefone', max_length=100)

	class Meta:
		verbose_name = 'Lead'
		verbose_name_plural = 'Leads'


	def __str__(self):
		return self.nome

class Contato(Base):
	assunto = models.CharField('Assunto', max_length=100)
	email = models.EmailField('Email')
	nome = models.CharField('Nome', max_length=100)
	mensagem = models.TextField('Mensagem', max_length=500)

	class Meta:
		verbose_name = 'Contato'
		verbose_name_plural = 'Contatos'


	def __str__(self):
		return self.nome



#telefone = models.CharField('Telefone', max_length=100)
#cpf = models.CharField('CPF/CNPJ', max_length=20)