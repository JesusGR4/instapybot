from django.shortcuts import render

from web.models import InstagramAccount
from django.db.models import Q

def home(request):
    """
    We are going to load all Instagram Account from User, If it hasnt, we will recommend him to create one
    :param request:
    :return:
    """
    context = {}
    if request.user.is_authenticated:
        instagram_accounts = InstagramAccount.objects.filter(user_id=request.user.pk)
        context['instagram_accounts'] = instagram_accounts
    return render(request, 'home.html', context)
