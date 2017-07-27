from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from apps.autor.forms import ConfiguracionForm
from apps.autor.models import *
from apps.post.models import *


def indexAutors(request, v):
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	autor = Perfil.objects.filter(activo=True, bloqueo=True).order_by('user__first_name')
	paginator = Paginator(autor, 15)
	try:
		page = int(v)
	except:
		page = 1
	try:
		autor = paginator.page(page)
	except (EmptyPage, InvalidPage):
		autor = paginator.page(paginator.num_pages)
	us = 'Home'
	uslink = '/'
	vs = 'Autor'
	context = {
		'categorias':categorias,
		'autor':autor,
		'us':us,
		'uslink':uslink,
		'vs':vs,
	}
	return render(request, 'autor/autores.html', context)


def indexAutor(request, v, w):
#	usuario = User.objects.get(username=v)
	categoria = User.objects.get(username=v)
	usuario = User.objects.get(username=v)
	autor = Perfil.objects.filter(user=usuario)
	postcount = Post.objects.filter(autor=autor, activo=True, bloqueo=True).count()
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	posts = Post.objects.filter(autor=autor, activo=True, bloqueo=True).order_by('-fechacreado')
	paginator = Paginator(posts, 10)
	try:
		page = int(w)
	except:
		page = 1
	try:
		post = paginator.page(page)
	except (EmptyPage, InvalidPage):
		post = paginator.page(paginator.num_pages)
	link = Post.objects.filter(autor=autor, activo=True, bloqueo=True).order_by('-vistas')[:10]
	link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
	seguido = Siguiendo.objects.filter(seguido=usuario.id)
	seguidocount = Siguiendo.objects.filter(seguido=usuario.id).count()
	siguiendo = Siguiendo.objects.filter(siguiendo=usuario.id)
	siguiendocount = Siguiendo.objects.filter(siguiendo=usuario.id).count()
	us = 'Home'
	uslink = '/'
	vs = 'Autor'
	vslink = '/autor/1/'
	ws = categoria.first_name+' '+categoria.last_name
	xs = page
	context = {
		'categoria':categoria,
		'categorias':categorias,
		'usuario':usuario,
		'post':post,
		'autor':autor,
		'postcount':postcount,
		'link':link,
		'link2':link2,
		'seguido':seguido,
		'seguidocount':seguidocount,
		'siguiendo':siguiendo,
		'siguiendocount':siguiendocount,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'vslink':vslink,
		'ws':ws,
		'xs':xs,
	}
	return render(request, 'autor/index.html', context)


def indexConfiguracion(request):
	if request.user.is_authenticated():
		mensaje = ''
		if request.method == "POST":
			form = ConfiguracionForm(request.POST)
			if form.is_valid():
				user = form.cleaned_data['user']
				photo = form.cleaned_data['photo']
				estado = form.cleaned_data['estado']
				pais = form.cleaned_data['pais']
				ciudad = form.cleaned_data['ciudad']
				direccion = form.cleaned_data['direccion']
				telefono = form.cleaned_data['telefono']
				fax = form.cleaned_data['fax']
				celular = form.cleaned_data['celular']
				web = form.cleaned_data['web']
				facebook = form.cleaned_data['facebook']
				twitter = form.cleaned_data['twitter']
				youtube = form.cleaned_data['youtube']
				linkedin = form.cleaned_data['linkedin']
				google = form.cleaned_data['google']
				pinterest = form.cleaned_data['pinterest']
				instagram = form.cleaned_data['instagram']
				blogger = form.cleaned_data['blogger']
				activo = form.cleaned_data['activo']
				if not user.is_authenticated and user.is_active:
					return HttpResponseRedirect('/configuracion/')
				else:
					alert = 'danger'
					mensaje = 'Datos no actualizados'
		form = ConfiguracionForm()
		usuario = request.user
		user = User.objects.get(username=usuario)
		pais = Pais.objects.all()
		usuario = Perfil.objects.get(user=user.id)
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
		us = 'Home'
		uslink = '/'
		vs = user.first_name + ' ' + user.last_name
		vslink = '/autor/' + user.username + '/'
		ws = 'Configuración'
		context = {
			'categorias':categorias,
			'usuario':usuario,
			'pais':pais,
			'link2':link2,
			'us':us,
			'uslink':uslink,
			'vs':vs,
			'vslink':vslink,
			'ws':ws,
		}
		return render(request, 'autor/configuracion.html', context)
	else:
		return HttpResponseRedirect('/')