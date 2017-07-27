from django.db import models
from django.contrib.auth.models import User


class Pais(models.Model):
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=3)
	indicativo = models.IntegerField()
	link = models.CharField(max_length=20)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['nombre']


class Perfil(models.Model):
	user = models.OneToOneField(User)
	ciudad = models.CharField(max_length=100, null=True, blank=True)
	estado = models.CharField(max_length=100, null=True, blank=True)
	pais = models.ForeignKey(Pais)
	direccion = models.TextField(max_length=300, null=True, blank=True)
	telefono = models.CharField(max_length=20, null=True, blank=True)
	fax = models.CharField(max_length=20, null=True, blank=True)
	celular = models.CharField(max_length=20, null=True, blank=True)
	web = models.URLField(null=True, blank=True)
	facebook = models.CharField(max_length=255, null=True, blank=True)
	twitter = models.CharField(max_length=255, null=True, blank=True)
	youtube = models.CharField(max_length=255, null=True, blank=True)
	linkedin = models.CharField(max_length=255, null=True, blank=True)
	google = models.CharField(max_length=255, null=True, blank=True)
	pinterest = models.CharField(max_length=255, null=True, blank=True)
	instagram = models.CharField(max_length=255, null=True, blank=True)
	blogger = models.CharField(max_length=255, null=True, blank=True)
	activo = models.BooleanField(default=False)
	bloqueo = models.BooleanField(default=True)

	def __str__(self):
		return self.user.username


class Siguiendo(models.Model):
	siguiendo = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	seguido = models.ForeignKey(Perfil, null=True, blank=True, on_delete=models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return '%s | %s | %s' % (self.fecha, self.siguiendo, self.seguido)

	class Meta:
		ordering = ['-fecha']