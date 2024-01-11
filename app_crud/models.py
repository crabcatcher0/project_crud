from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length = 300)
    description = models.CharField(max_length = 600)
    name = models.CharField(max_length = 50, default = 'TJMC')


class FrontPage(models.Model):
    phone_number1 = models.CharField(max_length=20, null=True, blank=True)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)
    phone_number3 = models.CharField(max_length=20, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)

class FrontPageOffice(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='official_bearer/')

    def __str__(self):
        return self.name
