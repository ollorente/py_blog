from django import forms
from django.contrib.auth.models import User

from apps.post.models import Post


class ComentarioForm(forms.Form):
	post = forms.IntegerField(widget=forms.TextInput())
	usuario = forms.IntegerField(widget=forms.TextInput())
	comentario = forms.CharField(widget=forms.TextInput())
	fecha = forms.DateTimeField(widget=forms.TextInput())