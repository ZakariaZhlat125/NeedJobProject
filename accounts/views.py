from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
User = settings.AUTH_USER_MODEL

def login(request):
    return render(request, 'accounts/login.html')

class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name='signup.html'


def get_success_urls(request):
    """
    Handle Success Url After Login
    """
    if 'next' in request.GET and request.GET['next'] != '':
        return request.GET['netx']
    else:
        return reverse('candidates:home')


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
