from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'accounts/login.html')


@login_required
def account(request):
    context = {
        'account_page': "active",
    }
    return render(request, 'accounts/account.html', context)


def privacy(request):
    return render(request, 'accounts/privacy.html')


def terms(request):
    return render(request, 'accounts/terms.html')


def pricing(request):
    context = {
        'rec_navbar': 1,
    }
    return render(request, 'accounts/pricing.html', context)
