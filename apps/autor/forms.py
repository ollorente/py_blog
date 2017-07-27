from django import forms
from django.contrib.auth.models import User


class ConfiguracionForm(forms.Form):
	user = forms.CharField(widget=forms.TextInput())
	estado = forms.CharField(widget=forms.TextInput())
	pais = forms.CharField(widget=forms.TextInput())
	ciudad = forms.CharField(widget=forms.TextInput())
	direccion = forms.CharField(widget=forms.TextInput())
	telefono = forms.CharField(widget=forms.TextInput())
	fax = forms.CharField(widget=forms.TextInput())
	celular = forms.CharField(widget=forms.TextInput())
	web = forms.URLField(widget=forms.TextInput())
	facebook = forms.CharField(widget=forms.TextInput())
	twitter = forms.CharField(widget=forms.TextInput())
	youtube = forms.CharField(widget=forms.TextInput())
	linkedin = forms.CharField(widget=forms.TextInput())
	google = forms.CharField(widget=forms.TextInput())
	pinterest = forms.CharField(widget=forms.TextInput())
	instagram = forms.CharField(widget=forms.TextInput())
	blogger = forms.CharField(widget=forms.TextInput())
	activo = forms.BooleanField(widget=forms.TextInput())