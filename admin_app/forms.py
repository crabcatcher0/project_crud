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