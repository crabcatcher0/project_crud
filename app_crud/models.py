from django.db import models

# Create your models here.

class Notice(models.Model):
    image = models.ImageField(upload_to='latest_events/', null=False)
    title = models.CharField(max_length = 300, null=False)
    description = models.CharField(max_length = 2000)
    posted_by = models.CharField(max_length = 50, default = 'TJMC')

    def __str__(self):
        return self.title


class ContactNumber(models.Model):
    phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.phone_number
    
    


class FrontPageOffice(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='official_bearer/')

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to='college_picture/', null=False, blank=False, default='noimg.jpg')
    title = models.CharField(max_length = 200, null=True, blank = True)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    about_us_description = models.CharField(max_length = 3000, default='This is About Us Section.')
    image = models.ImageField(upload_to='about_us/', null=True)

    def save(self, *args, **kwargs):
        # Check if an instance already exists
        if AboutUs.objects.exists() and not self.pk:
            existing_instance = AboutUs.objects.first()
            existing_instance.about_us_description = self.about_us_description
            existing_instance.image = self.image
            existing_instance.save()
            return existing_instance
        else:
            return super().save(*args, **kwargs)

    def __str__(self):
        return "About Us"
    
    class Meta:
        verbose_name_plural = "About Us"