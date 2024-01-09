from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length = 300)
    description = models.CharField(max_length = 600)
    name = models.CharField(max_length = 50, default = 'TJMC')