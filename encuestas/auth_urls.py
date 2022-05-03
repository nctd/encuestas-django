from django.urls import path
from .views.auth import login_user, registro

urlpatterns = [
    path('login_user',login_user,name='login'),
    path('registro', registro, name='registro')
]