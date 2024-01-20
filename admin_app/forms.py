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


class LeaderForm(forms.ModelForm):
    class Meta:
        model = FrontPageOffice
        fields = ['name', 'position', 'image']


class Plus2Form(forms.ModelForm):
    class Meta:
        model = Plus2
        fields = ['course_title', 'course_description', 'affiliation', 'duration', 'eligibility', 'career', 'course_summary', 'course_file']


class BachelorForm(forms.ModelForm):
    class Meta: 
        model = Bachelor
        fields = ['course_title', 'course_description', 'affiliation', 'duration', 'eligibility', 'career', 'course_summary', 'course_file']


class MasterForm(forms.ModelForm):
    class Meta:
        model = MasterProgram
        fields = ['course_title', 'course_description', 'affiliation', 'duration', 'eligibility', 'career', 'course_summary', 'course_file']

class DownloadableForm(forms.ModelForm):
    class Meta:
        model = DownloadableFile
        fields = ['file_title', 'actual_file']
