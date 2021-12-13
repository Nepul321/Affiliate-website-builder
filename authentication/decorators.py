from django.http.response import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def not_active_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_active:
			return redirect('/')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def have_purchased(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.purchased == False and request.user.is_superuser == False:
			return view_func(request, *args, **kwargs)
		else:
			return redirect('dashboard')
		
	return wrapper_func

def have_access(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.purchased == True or request.user.is_superuser:
			return view_func(request, *args, **kwargs)
		else:
			return redirect('purchase')

	return wrapper_func