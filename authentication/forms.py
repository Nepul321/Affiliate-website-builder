from django.contrib.auth.forms import (
	UserCreationForm,
	UserChangeForm
	)
from django import forms
from base.models import User

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class' : 'form-control'})
		self.fields['email'].widget.attrs.update({'class' : 'form-control'})
		self.fields['name'].widget.attrs.update({'class' : 'form-control'})
		self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['password2'].widget.attrs.update({'class' : 'form-control'})

class AccountForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'name')

		widgets = {
          'username' : forms.TextInput(attrs={'class' : 'form-control'}),
          'email' : forms.EmailInput(attrs={'required' : '', 'class' : 'form-control'}),
          'name' : forms.TextInput(attrs={'required' : '', 'class' : 'form-control'}),

		}