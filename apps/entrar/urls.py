from django.conf.urls import url

from apps.entrar.views import login_view, logout_view

urlpatterns = [
	url(r'^$', login_view, name='vista_login'),
	url(r'^/$', logout_view, name='vista_logout'),
]