from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from web.forms import  InstagramAccountForm


def create(request):
    """
    Show a user register form
    :param request: HttpRequest
    :return: HttpResponse
    """
    if request.method == 'GET':
        form = InstagramAccountForm()
    else:
        form = InstagramAccountForm(request.POST)
        if form.is_valid():
            new_user = form.save()  # We are gonna save the object and it will be back
            messages.add_message(request,messages.INFO,_('You have been registered succesfully!'))
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'user/signup.html', context)