from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admission_number/', admission_number, name='admission_number'),
]