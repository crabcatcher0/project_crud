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
    path('delect_contact_numbers/<int:id>/', delete_contact_number, name='delete_contact_numbers'),
    path('confirmation_page_contact/<int:id>/', confirmation_page_contact, name='confirmation_page_contact'),
    path('notice_admin/', notice_admin, name='notice_admin'),
    path('delete_notice/<int:id>/', delete_notice, name='delete_notice'),
    path('confirm_delete_notice/<int:id>/', confirmation_delete_notice, name='confirm_delete_notice'),
    path('gallery_admin/', gallery_admin, name='gallery_admin'),
    path('delete_gallery/<int:id>/', delete_gallery, name='delete_gallery'),
    path('confirm_delete_image/<int:id>/', confirm_delete_image, name='confirm_delete_image'),
    path('leaders_admin', leaders_admmin, name='leaders_admin'),
    path('delete_leaders/<int:id>/', delete_leaders, name='delete_leaders'),
    path('confirm_delete_leaders/<int:id>/', confirm_delete_leaders, name='confirm_delete_leaders'),






]