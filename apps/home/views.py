from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from apps.autor.models import *
from apps.post.models import *


def indexHome(request):
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	# pricategoria = Categoria.objects.get(id=5, activo=True, bloqueo=True)
	# principal = Post.objects.filter(categoria=pricategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	notcategoria = Categoria.objects.get(id=2, activo=True, bloqueo=True)
	noticia = Post.objects.filter(categoria=notcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	opicategoria = Categoria.objects.get(id=1, activo=True, bloqueo=True)
	opinion = Post.objects.filter(categoria=opicategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	alocategoria = Categoria.objects.get(id=3, activo=True, bloqueo=True)
	aloido = Post.objects.filter(categoria=alocategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	humcategoria = Categoria.objects.get(id=4, activo=True, bloqueo=True)
	humor = Post.objects.filter(categoria=humcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	regcategoria = Categoria.objects.get(id=6, activo=True, bloqueo=True)
	region = Post.objects.filter(categoria=regcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	intcategoria = Categoria.objects.get(id=7, activo=True, bloqueo=True)
	internacional = Post.objects.filter(categoria=intcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	vidcategoria = Categoria.objects.get(id=9, activo=True, bloqueo=True)
	video = Post.objects.filter(categoria=vidcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	entcategoria = Categoria.objects.get(id=8, activo=True, bloqueo=True)
	entrevista = Post.objects.filter(categoria=entcategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	percategoria = Categoria.objects.get(id=5, activo=True, bloqueo=True)
	personaje = Post.objects.filter(categoria=percategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	ecocategoria = Categoria.objects.get(id=10, activo=True, bloqueo=True)
	ecosbogota = Post.objects.filter(categoria=ecocategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	teccategoria = Categoria.objects.get(id=11, activo=True, bloqueo=True)
	tecnologia = Post.objects.filter(categoria=teccategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	ecncategoria = Categoria.objects.get(id=12, activo=True, bloqueo=True)
	economia = Post.objects.filter(categoria=ecncategoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:3]
	link = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
	us = 'Home'
	context = {
		'categorias':categorias,
		# 'pricategoria':pricategoria,
		# 'principal':principal,
		'notcategoria':notcategoria,
		'noticia':noticia,
		'opicategoria':opicategoria,
		'opinion':opinion,
		'alocategoria':alocategoria,
		'aloido':aloido,
		'humcategoria':humcategoria,
		'humor':humor,
		'regcategoria':regcategoria,
		'region':region,
		'intcategoria':intcategoria,
		'internacional':internacional,
		'vidcategoria':vidcategoria,
		'video':video,
		'entcategoria':entcategoria,
		'entrevista':entrevista,
		'percategoria':percategoria,
		'personaje':personaje,
		'ecocategoria':ecocategoria,
		'ecosbogota':ecosbogota,
		'teccategoria':teccategoria,
		'tecnologia':tecnologia,
		'ecncategoria':ecncategoria,
		'economia':economia,
		'link':link,
		'us':us,
	}
	return render(request, 'home/index.html', context)