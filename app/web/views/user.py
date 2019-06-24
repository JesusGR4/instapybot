from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.utils.translation import ugettext_lazy as _
from django.contrib.sessions.models import Session
from django.contrib import messages
from web.forms import LoginForm, UserForm
from django.views.generic import View


class SignupView(View):
    def get(self, request):
        """
        Show a user register form
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = UserForm()
        context = {
            'form': form,
        }
        return render(request, 'user/signup.html', context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()  # We are gonna save the object and it will be back
            messages.add_message(request, messages.INFO, _('You have been registered succesfully!'))
            return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'user/signup.html', context)


class LoginView(View):
    error_messages = []
    context = {}
    def get(self, request):
        form = LoginForm()
        self.context = {
            'errors': self.error_messages,
            'form': form
        }
        return render(request, 'user/login.html', self.context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            user = authenticate(username=username, password=password)
            if user is None:
                self.error_messages.append(_('User does not exist'))
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect('home')
                else:
                    self.error_messages.append(_('User not active'))
        self.context = {
            'errors': self.error_messages,
            'form': form
        }
        return render(request, 'user/login.html', self.context)


# This controller is gonna handle if the user is logged, if it's, it logs out it and resend to the home
def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('home')
