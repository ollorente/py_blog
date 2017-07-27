from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from apps.entrar.forms import LoginForm
from apps.autor.models import Pais, Perfil
from apps.post.models import Post, Categoria


def login_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		mensaje = ""
		if request.user.is_authenticated():
			return HttpResponseRedirect('/blog/')
		else:
			if request.method == "POST":
				form = LoginForm(request.POST)
				if form.is_valid():
					username = form.cleaned_data['username']
					password = form.cleaned_data['password']
					usuario = authenticate(username=username, password=password)
					if usuario is not None and usuario.is_active:
						login(request, usuario)
						return HttpResponseRedirect('/blog/1/')
					else:
						alert = 'danger'
						mensaje = 'Usuario y/o password incorrecto'
			form = LoginForm()
			categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
			link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
			us = 'Home'
			uslink = '/'
			vs = 'Entrar'
			context = {
				'categorias':categorias,
				'link2':link2,
				'us':us,
				'uslink':uslink,
				'vs':vs,
				'form':form,
				'mensaje':mensaje,
			}
			return render(request, 'entrar/index.html', context)


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')