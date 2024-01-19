from django.db import models
from django.utils import timezone
# Create your models here.

class Notice(models.Model):
    image = models.ImageField(upload_to='latest_events/', blank=True)
    title = models.CharField(max_length = 300, null=False)
    description = models.CharField(max_length = 2000)
    posted_by = models.CharField(max_length = 50, default = 'TJMC')
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_created_at(self):
        return timezone.localtime(self.created_at).strftime('%Y-%m-%d')


    def __str__(self):
        return self.title


class ContactNumber(models.Model):
    phone_number = models.CharField(max_length=20, default='TJMC')

    def __str__(self):
        return self.phone_number
    

class AdmissionNumber(models.Model):
    admission_number = models.CharField(max_length=20, default='TJMC')

    def __str__(self):
        return self.admission_number
    
    


class FrontPageOffice(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='official_bearer/')

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to='college_picture/', null=False, blank=False)
    title = models.CharField(max_length = 200, null=True, blank = True, default='TJMC')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Plus2(models.Model):
    course_title = models.CharField(max_length=100, default ='SomeDefaultTitle')
    course_description = models.CharField(max_length=2000, default='SomeDefaultDescription')
    affiliation = models.CharField(max_length=100, null=True, default='TU')
    duration = models.CharField(max_length=300, default='SomeDefaultDuration')
    eligibility = models.CharField(max_length=300, default='SomeDefaultDuration')
    career = models.CharField(max_length=1000, default='DefaultCareer')
    course_summary = models.CharField(max_length=2000, default='DefaultSummary')
    course_file = models.FileField(upload_to='course_files/', null=True, blank=True)


    def __str__(self):
        return self.course_title
    
class Bachelor(models.Model):
    course_title = models.CharField(max_length=100, default ='SomeDefaultTitle')
    course_description = models.CharField(max_length=2000, default='SomeDefaultDescription')
    affiliation = models.CharField(max_length=100, null=True, default='TU')
    duration = models.CharField(max_length=300, default='SomeDefaultDuration')
    eligibility = models.CharField(max_length=300, default='SomeDefaultDuration')
    career = models.CharField(max_length=1000, default='DefaultCareer')
    course_summary = models.CharField(max_length=2000, default='DefaultSummary')
    course_file = models.FileField(upload_to='course_files/', null=True, blank=True)


    def __str__(self):
        return self.course_title
    

class MasterProgram(models.Model):
    course_title = models.CharField(max_length=100, default ='SomeDefaultTitle')
    course_description = models.CharField(max_length=2000, default='SomeDefaultDescription')
    affiliation = models.CharField(max_length=100, null=True, default='TU')
    duration = models.CharField(max_length=300, default='SomeDefaultDuration')
    eligibility = models.CharField(max_length=300, default='SomeDefaultDuration')
    career = models.CharField(max_length=1000, default='DefaultCareer')
    course_summary = models.CharField(max_length=2000, default='DefaultSummary')
    course_file = models.FileField(upload_to='master_files/', null=True, blank=True)


    def __str__(self):
        return self.course_title
    

class DownloadableFile(models.Model):
    file_title = models.CharField(max_length = 500)
    actual_file = models.FileField(upload_to='downloadable_files/', null=False, blank=False)

    def __str__(self):
        return self.file_title
    

class ContactUs(models.Model):
    fullName = models.CharField(max_length = 30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length = 30)
    message = models.CharField(max_length = 300)

    def __str__(self):
        return self.fullName
