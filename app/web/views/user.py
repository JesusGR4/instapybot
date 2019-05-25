from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.utils.translation import ugettext_lazy as _
from django.contrib.sessions.models import Session


def signup(request):
    pass


def login(request):
    error_messages = []
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is None:
            error_messages.append(_('User does not exist'))
        else:
            if user.is_active:
                django_login(request, user)
                return redirect('home')
            else:
                error_messages.append(_('User not active'))

    context = {
        'errors': error_messages
    }

    return render(request, 'user/login.html', context)


# This controller is gonna handle if the user is logged, if it's, it logs out it and resend to the home
def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('home')
