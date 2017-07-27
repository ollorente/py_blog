from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from apps.autor.models import *
from apps.post.models import *


def indexCategoria(request, u, v):
	categoria = Categoria.objects.get(slug=u, activo=True, bloqueo=True)
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	posts = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-fechacreado')
	paginator = Paginator(posts, 10)
	try:
		page = int(v)
	except:
		page = 1
	try:
		post = paginator.page(page)
	except (EmptyPage, InvalidPage):
		post = paginator.page(paginator.num_pages)
	link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-vistas')[:10]
	link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
	us = 'Home'
	uslink = '/'
	vs = categoria.titulo
	ws = page
	context = {
		'categoria':categoria,
		'categorias':categorias,
		'post':post,
		'link':link,
		'link2':link2,
		'us':us,
		'uslink':uslink,
		'vs':vs,
		'ws':ws,
	}
	return render(request, 'categoria/index.html', context)