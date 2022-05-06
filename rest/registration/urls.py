from django.contrib import path

from .views import auth
from . import views

urlpatterns = [
    path('auth', views.auth, name='new_user')
]