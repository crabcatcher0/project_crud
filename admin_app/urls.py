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
    path('plus2_admin', plus2_admin, name='plus2_admin'),
    path('delete_plus2/<int:id>/', delte_plus2, name='delete_plus2'),
    path('confirm_delete_plus2/<int:id>/', confirm_delete_plus2, name='confirm_delete_plus2'),
    path('bachelor_admin', bachelor_admin, name='bachelor_admin'),
    path('delete_bachelor/<int:id>/', delete_bachelor, name='delete_bachelor'),
    path('confirm_delete_bachelor/<int:id>/', confirm_delete_bachelor, name='confirm_delete_bachelor'),
    path('master_admin', master_admin, name='master_admin'),
    path('delete_master/<int:id>/', delete_master, name='delete_master'),
    path('confirm_delete_master/<int:id>/', confirm_delete_master, name='confirm_delete_master'),
    path('downloads_admin', downloads_admin, name='downloads_admin'),
    path('delete_downloads/<int:id>/', delete_downloads, name='delete_downloads'),
    path('confirm_delete_downloads/<int:id>/', confirm_delete_downloads, name='confirm_delete_downloads'),










]