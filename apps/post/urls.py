from django.conf.urls import patterns, include, url

from apps.post.views import indexPost, crearPost


urlpatterns = [
	url(r'^$', indexPost, name="vista_post"),
	url(r'^/$', crearPost, name="vista_crearpost"),
]