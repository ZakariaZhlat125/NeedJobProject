from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView
from .forms import UserRegistrationForm,UserLoginForm

User = settings.AUTH_USER_MODEL



def get_success_urls(request):
    """
    Handle Success Url After Login
    """
    if 'next' in request.GET and request.GET['next'] != '':
        return request.GET['next']
    else:
        return reverse('candidates:home')

def login(request):
    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        return redirect('/')

    else:
        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return HttpResponseRedirect(get_success_urls(request))
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html',context)


def user_registration(request):
    """
    Handle user registration
    """
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('accounts:login')
    context = {
        'form': form,
    }
    return render(request, 'accounts/user-registration.html', context)




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
