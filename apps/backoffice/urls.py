from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from apps.backoffice.views import indexBackoffice

urlpatterns = [
	url(r'^$', indexBackoffice, name="vista_backoffice"),
]