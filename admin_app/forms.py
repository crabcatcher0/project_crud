from django import forms
from app_crud.models import *


class AdmissionNumberForm(forms.ModelForm):
    class Meta:
        model = AdmissionNumber
        fields = ['admission_number']


class ContactNumberForm(forms.ModelForm):
    class Meta:
        model = ContactNumber
        fields = ['phone_number']


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['image', 'title', 'description', 'posted_by']


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image', 'title']