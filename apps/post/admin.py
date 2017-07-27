from django.contrib import admin
from django.contrib.auth.models import User

from apps.post.models import *
from apps.autor.models import *


admin.site.register(Tipoacceso)
admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Megusta)


class TipoaccesoAdmin(admin.ModelAdmin):
	list_display = ('nombre')
	list_display_links = ('nombre')
	class Meta:
		ordering = ('nombre',)


class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('titulo')
	list_display_links = ('titulo')
	class Meta:
		ordering = ('titulo',)


class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'slug')
	search_field = ('titulo',)
	list_display_links = ('titulo')
	prepopulated_fields = {'slug': ('titulo',)}

	class Meta:
		ordering = ('titulo',)


class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'post', 'usuario',)

	class Meta:
		ordering = ('fecha', 'post', 'usuario',)


class MegustaAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'graf', 'usuario',)

	class Meta:
		ordering = ('fecha', 'graf', 'usuario',)