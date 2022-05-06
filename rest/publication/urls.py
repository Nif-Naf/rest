from django.contrib import path
from . import views

urlpatterns = [
    path('reseve_publicateon', views.reseve, name='reseve_pub' )
]