from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario", widget=forms.TextInput())
	first_name = forms.CharField(label="Nombre(s)", widget=forms.TextInput())
	last_name = forms.CharField(label="Apellido(s)", widget=forms.TextInput())
	email = forms.EmailField(label="Email", widget=forms.TextInput())
	password_one = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar Password", widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username = username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe.')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado.')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']

		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')