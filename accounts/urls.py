from django.urls import path

from accounts import views
app_name= 'accounts'

urlpatterns = [
    path('accounts/register/', views.user_registration, name='user-register'),
    #path('login/',views.login, name='login'),
]