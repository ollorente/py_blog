from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from apps.autor.models import *
from apps.post.models import *


def indexBlog(request, v):
	if request.user.is_authenticated():
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
#		post = Siguiendo.objects.filter(siguiendo=request.user)
		posts = Post.objects.filter(activo=True, bloqueo=True).order_by('-fechacreado')
		paginator = Paginator(posts, 10)
		try:
			page = int(v)
		except:
			page = 1
		try:
			post = paginator.page(page)
		except (EmptyPage, InvalidPage):
			post = paginator.page(paginator.num_pages)
		link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
#		seguido = Siguiendo.objects.filter(seguido=user.id)[:25]
#		seguidocount = Siguiendo.objects.filter(seguido=user.id).count()
#		siguiendo = Siguiendo.objects.filter(siguiendo=user.id)[:25]
#		siguiendocount = Siguiendo.objects.filter(siguiendo=user.id).count()
		us = 'Home'
		uslink = '/'
		vs = 'Blog'
		ws = page
		context = {
			'categorias':categorias,
			'post':post,
			'link2':link2,
#			'seguido':seguido,
#			'seguidocount':seguidocount,
#			'siguiendo':siguiendo,
#			'siguiendocount':siguiendocount,
			'us':us,
			'uslink':uslink,
			'vs':vs,
			'ws':ws,
		}
		return render(request, 'blog/index.html', context)
	else:
		return HttpResponseRedirect('/')