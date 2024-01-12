from django.db import models

# Create your models here.

class Notice(models.Model):
    image = models.ImageField(upload_to='latest_events/', null=True)
    title = models.CharField(max_length = 300, null=False)
    description = models.CharField(max_length = 2000)
    posted_by = models.CharField(max_length = 50, default = 'TJMC')

    def __str__(self):
        return self.title


class ContactNumber(models.Model):
    phone_number = models.CharField(max_length=20, null=True)
    
    


class FrontPageOffice(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='official_bearer/')

    def __str__(self):
        return self.name
    


