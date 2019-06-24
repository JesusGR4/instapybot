# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from web.forms import InstagramAccountForm
from django.contrib.auth.decorators import login_required

from web.models import InstagramAccount
from django.views.generic import View


class CreateInstagramAccountView(View):
    context = {}
    error_messages = []

    @method_decorator(login_required())
    def get(self, request):
        form = InstagramAccountForm()
        self.context = {
            'form': form,
        }
        return render(request, 'user/signup.html', self.context)

    @method_decorator(login_required())
    def post(self, request):
        instagram_account = InstagramAccount()
        instagram_account.user = request.user
        form = InstagramAccountForm(request.POST, instance=instagram_account)
        if form.is_valid():
            new_user = form.save()  # We are gonna save the object and it will be back
            messages.add_message(request, messages.INFO, _('You have been registered succesfully!'))
            return redirect('login')

        self.context = {
            'form': form,
        }
        return render(request, 'user/signup.html', self.context)
