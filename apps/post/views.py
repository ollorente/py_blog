from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from apps.post.forms import ComentarioForm
from apps.autor.models import *
from apps.post.models import *


def indexPost(request, u, v, w):
	if request.user.is_authenticated():
		url = '/' + u + '/' + v + '/' + w + '/'
		form = ComentarioForm()
		if request.method == "POST":
			form = ComentarioForm(request.POST)
			if form.is_valid():
				form.save()
#				post = form.cleaned_data['post']
#				usuario = form.cleaned_data['usuario']
#				comentario = form.cleaned_data['comentario']
#				fecha = form.cleaned_data['fecha']
#				u = Post.objects.creationform(post=post, usuario=usuario, comentario=comentario, fecha=fecha)
#				u.save()
				return HttpResponseRedirect(url)
			else:
				return HttpResponseRedirect(url)

	cat = Categoria.objects.filter(menu=1)
	acceso = Tipoacceso.objects.all()
	categoria = Categoria.objects.get(slug=u, activo=True, bloqueo=True)
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	post = Post.objects.get(id=v, activo=True, bloqueo=True)
	comentario = Comentario.objects.filter(post=v)[:10]
	comentariocount = Comentario.objects.filter(post=v).count()
	link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-vistas')[:10]
	megustacount = Megusta.objects.filter(graf=v).count()
	us = 'Home'
	uslink = '/'
	vs = categoria.titulo
	vslink = '/' + categoria.slug + '/1/'
	ws = post.titulo
	context = {
		'cat':cat,
		'acceso':acceso,
		'categoria':categoria,
		'categorias':categorias,
		'post':post,
		'comentario':comentario,
		'comentariocount':comentariocount,
		'link':link,
		'megustacount':megustacount,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'vslink':vslink,
		'ws':ws,
	}
	return render(request, 'post/index.html', context)


def crearPost(request):
	if request.user.is_authenticated():
		cat = Categoria.objects.filter(menu=1)
		acceso = Tipoacceso.objects.all()
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
		us = 'Home'
		uslink = '/'
		vs = 'Crear post'
		context = {
			'cat':cat,
			'acceso':acceso,
			'categorias':categorias,
			'link2':link2,
			'us':us,
			'uslink':uslink,
			'vs':vs,
		}
		return render(request, 'post/crear.html', context)
	else:
		return HttpResponseRedirect('/')

"""
def indexPost(request, u, v, w):
	if request.user.is_authenticated():
		mensaje = ''
		posts = int(13)
		usuario = User
		comentar = 'comentar'
		fecha = '2017-07-17 14:02:53'
		url = '/' + u + '/' + v + '/' + w + '/'
		if request.method == "POST":
			form = ComentarioForm(request.POST)
			if form.is_valid():
				post = form.cleaned_data['posts']
				usuario = form.cleaned_data[user.id]
				comentario = form.cleaned_data['comentar']
				fecha = form.cleaned_data['fecha']
				form.save()
				return HttpResponseRedirect(url)
			else:
				alert = 'danger'
				mensaje = 'Comentario no enviado'
		else:
			form = ComentarioForm()
			alert = 'danger'
			mensaje = 'Comentario no enviado'

	cat = Categoria.objects.filter(menu=1)
	acceso = Tipoacceso.objects.all()
	categoria = Categoria.objects.get(slug=u, activo=True, bloqueo=True)
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	post = Post.objects.get(id=v, activo=True, bloqueo=True)
	comentario = Comentario.objects.filter(post=v)[:10]
	comentariocount = Comentario.objects.filter(post=v).count()
	link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-vistas')[:10]
	megustacount = Megusta.objects.filter(graf=v).count()
	us = 'Home'
	uslink = '/'
	vs = categoria.titulo
	vslink = '/'+categoria.slug+'/'
	ws = post.titulo
	context = {
		'cat':cat,
		'acceso':acceso,
		'categoria':categoria,
		'categorias':categorias,
		'post':post,
		'comentario':comentario,
		'comentariocount':comentariocount,
		'link':link,
		'megustacount':megustacount,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'vslink':vslink,
		'ws':ws,
	}
	return render(request, 'post/index.html', context)


def formComentario(request, u, v, w):
	if request.user.is_authenticated():
		mensaje = ''
		post = 'comentar'
		comentar = 'comentar'
		if request.method == "POST":
			form = ConfiguracionForm(request.POST)
			if form.is_valid():
				form.save()
#				return HttpResponseRedirect('/configuracion/')
#				post = form.cleaned_data['post']
#				usuario = form.cleaned_data[user.id]
#				comentario = form.cleaned_data[comentar]
#				fecha = form.cleaned_data['']
#				if not user.is_authenticated and user.is_active:
#					return HttpResponseRedirect('/configuracion/')
#				else:
#					alert = 'danger'
#					mensaje = 'Comentario no enviado'
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
"""