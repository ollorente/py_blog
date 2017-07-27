from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from apps.autor.views import *

urlpatterns = [
	url(r'^', indexAutor, name='vista_autor'),
	url(r'^$', indexAutors, name='vista_autors'),
	url(r'^/$', login_required(indexConfiguracion), name='vista_configuracion'),
]