from django.conf.urls import url

from apps.registro.views import register_view


urlpatterns = [
	url(r'^$', register_view, name='vista_registro'),
]