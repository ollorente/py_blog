from django.contrib import admin
from django.contrib.auth.models import User

from apps.autor.models import *


admin.site.register(Pais)
admin.site.register(Perfil)
admin.site.register(Siguiendo)


class PaisAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'codigo', 'link', 'indicativo',)
	search_field = ['nombre']
	list_display_links = ('nombre')
	
	class Meta:
		ordering = ('nombre', 'codigo', 'link', 'indicativo',)


class PerfilAdmin(admin.ModelAdmin):
	list_display = ('usuario', 'ciudad', 'estado', 'pais',)
	search_field = ['usuario']
	list_display_links = ('usuario')
	fields = ('user', 'ciudad', 'estado', 'pais',)
	
	class Meta:
		ordering = ('usuario', 'ciudad', 'estado', 'pais',)


class SiguiendoAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'seguido', 'siguiendo',)

	class Meta:
		ordering = ('fecha', 'seguido', 'siguiendo',)