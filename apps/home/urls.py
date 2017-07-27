from django.conf.urls import url

from apps.home.views import indexHome

urlpatterns = [
	url(r'^$', indexHome, name='vista_home'),
]