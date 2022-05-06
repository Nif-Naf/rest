from django.contrib import path
from . import views

urlpatterns = [
    path('sign', views.sign, name='sign_get')
]