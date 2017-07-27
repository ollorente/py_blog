from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from apps.registro.forms import RegisterForm
from apps.autor.models import Pais, Perfil
from apps.post.models import Post, Categoria


def register_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		form = RegisterForm()
		if request.method == "POST":
			form = RegisterForm(request.POST)
			if form.is_valid():
				usuario = form.cleaned_data['username']
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				email = form.cleaned_data['email']
				password_one = form.cleaned_data['password_one']
				password_two = form.cleaned_data['password_two']
				u = User.objects.create_user(username=usuario, first_name=first_name, last_name=last_name, email=email, password=password_one)
				u.save()
				categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
				link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
				us = 'Home'
				uslink = '/'
				vs = 'Registro'
				context = {
					'categorias':categorias,
					'link2':link2,
					'us':us,
					'uslink':uslink,
					'vs':vs,
				}
				return render(request, 'registro/thanks_register.html', context)
			else:
				categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
				link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
				us = 'Home'
				uslink = '/'
				vs = 'Registro'
				context = {
					'categorias':categorias,
					'link2':link2,
					'us':us,
					'uslink':uslink,
					'vs':vs,
					'form':form,
				}
				return render(request, 'registro/index.html', context)
		categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
		link2 = Post.objects.filter(activo=True, bloqueo=True).order_by('-vistas')[:10]
		us = 'Home'
		uslink = '/'
		vs = 'Registro'
		context = {
			'categorias':categorias,
			'link2':link2,
			'us':us,
			'uslink':uslink,
			'vs':vs,
			'form':form,
		}
		return render(request, 'registro/index.html', context)