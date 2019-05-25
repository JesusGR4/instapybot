from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.utils.translation import ugettext_lazy as _
from django.contrib.sessions.models import Session

from web.forms import LoginForm


def signup(request):
    pass


# Login View, Here system handle User Authentication
def login(request):
    error_messages = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append(_('User does not exist'))
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect('home')
                else:
                    error_messages.append(_('User not active'))
    else:
        form = LoginForm()
    context = {
        'errors': error_messages,
        'form': form
    }
    return render(request, 'user/login.html', context)


# This controller is gonna handle if the user is logged, if it's, it logs out it and resend to the home
def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('home')
