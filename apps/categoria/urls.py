from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from apps.categoria.views import indexCategoria

urlpatterns = [
	url(r'^$', indexCategoria, name='vista_categoria'),
]