from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from apps.autor.models import *


class Tipoacceso(models.Model):
	tipo = models.CharField(max_length=50)

	def __str__(self):
		return self.tipo

	class Meta:
		ordering = ['tipo']


class Categoria(models.Model):
	titulo = models.CharField(max_length=140)
	slug = models.SlugField(max_length=140)
	menu = models.IntegerField(default=1)
	acceso = models.ForeignKey(Tipoacceso, null=True, blank=True, on_delete=models.CASCADE)
	activo = models.BooleanField(default=True)
	bloqueo = models.BooleanField(default=True)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['titulo']


class Post(models.Model):
	titulo = models.CharField(max_length=140)
	slug = models.SlugField(max_length=140, unique=True)
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
	contenido = models.TextField()
	autor = models.ForeignKey(Perfil)
	fechacreado = models.DateTimeField(auto_now_add=True, blank=True)
	fechainicio = models.DateTimeField(auto_now_add=True, blank=True)
	fechafinal = models.DateTimeField(auto_now_add=True, blank=True)
	fechamodificado = models.DateTimeField(auto_now_add=True, blank=True)
	acceso = models.ForeignKey(Tipoacceso, null=True, blank=True, on_delete=models.CASCADE)
	tags = models.TextField(null=True, blank=True)
	vistas = models.IntegerField(null=True, blank=True)
	activo = models.BooleanField(default=True)
	bloqueo = models.BooleanField(default=True)

	def slug(self):
		return slugify(self.titulo)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['titulo']


class Comentario(models.Model):
	post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
	usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	comentario = models.TextField(max_length=255)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return '%s | %s | %s' % (self.fecha, self.usuario, self.post)

	class Meta:
		ordering = ['-fecha']


class Megusta(models.Model):
	usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	graf = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return '%s | %s | %s' % (self.fecha, self.graf, self.usuario)

	class Meta:
		ordering = ['-fecha']