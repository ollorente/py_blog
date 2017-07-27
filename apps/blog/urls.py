from django.conf.urls import url

from apps.blog.views import indexBlog


urlpatterns = [
	url(r'^$', indexBlog, name='vista_blog'),
]