from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admission_number/', admission_number, name='admission_number'),
    path('delete_admission_number/<int:id>/', delete_admission_number, name='delete_admission_number'),
    path('confirmation/<int:id>/', delete_confirm, name='confirmation_page'),
    path('contact_numbers/', contact_numbers, name='contact_numbers'),
]