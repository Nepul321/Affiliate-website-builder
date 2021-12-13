from django.shortcuts import render, redirect
from .forms import (
    CreateUserForm,
    AccountForm,
)
from .decorators import (have_purchased, unauthenticated_user, not_active_user)
import uuid
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from base.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from src.settings import ALLOWED_HOSTS
from django.conf import settings


@unauthenticated_user
def SignupView(request):
    template = "signup.html"
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            key = uuid.uuid4()
            user = User.objects.get(email=request.POST['email'])
            user.key = key
            user.is_active = False
            user.save()
            subject = "Verify your email"
            message = f"Hi {user.name}, thank you for signing up. \n Please verify your email. \n http://{ALLOWED_HOSTS[0]}:8000/activate-account/{user.key}/"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            template2 = "email_sent.html"
            context2 = {}
            return render(request, template2, context2)
    
    context = {
        'form' : form,
    }

    return render(request, template, context)



@login_required
def PasswordView(request):
    template = "registration/password.html"
    form = PasswordChangeForm(user=request.user)
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('account')

    context = {'form': form}
    return render(request, template, context)


@login_required
def AccountView(request):
    template = "registration/account.html"
    form = AccountForm(instance=request.user)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, template, context)


@login_required
def UserDeleteView(request):
    template = "registration/delete-account.html"
    if request.method == "POST":
        current_user = request.user
        user_object = User.objects.get(id=current_user.id)
        user_object.delete()
        return redirect('home')

    context = {}
    return render(request, template, context)

@not_active_user
def ActivateAccountView(request, token):
	try:
		user = User.objects.get(key=token)
		user.is_active = True
		user.save()
	except:
		return redirect('/')
	template = 'activate.html'
	context = {}
	return render(request, template, context)

@login_required
@have_purchased
def purchaseview(request):
    template = 'payments/purchase.html'
    context = {}
    return render(request, template, context)