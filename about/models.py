from django.db import models

# Create your models here.

class About(models.Model):
    profile = models.CharField(max_length=255)
    visaun = models.TextField(max_length=455)
    misaun = models.TextField(max_length=455)
    service = models.TextField(max_length=255)


    def __str__(self):
        return "{}".format(self.profile)

