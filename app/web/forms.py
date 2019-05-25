from django import forms
from django.utils.translation import ugettext_lazy as _

from web.models import User


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
