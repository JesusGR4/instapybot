# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from web.models import User, InstagramAccount
from .validators.instagramvalidator import validate_instagram_account
from django.conf import settings
from cryptography.fernet import Fernet


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Username'))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput())


class UserForm(forms.ModelForm):
    """
    User form
    info: We have to re-define save function because we are not using a different User Form, so we have to set manually the password
    """

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class InstagramAccountForm(forms.ModelForm):

    def save(self, commit=True):
        instagram = super(InstagramAccountForm, self).save(commit=False)
        f = Fernet(settings.AES256_KEY)
        instagram.instagram_account_password = f.encrypt(
            bytes(self.cleaned_data.get(u'instagram_account_password'), encoding='utf8'))
        if commit:
            instagram.save()
        return instagram

    def clean(self):
        instagram_account_name = self.cleaned_data.get(u'instagram_account_name')
        instagram_account_password = self.cleaned_data.get(u'instagram_account_password')
        if not validate_instagram_account(instagram_account_name, instagram_account_password):
            raise ValidationError(_("Invalid login"))

        return self.cleaned_data

    """
    Instagram Account form
    """

    class Meta:
        model = InstagramAccount
        fields = ['name', 'instagram_account_name', 'instagram_account_password']
        exclude = ['user']
        widgets = {
            'instagram_account_password': forms.PasswordInput()
        }
