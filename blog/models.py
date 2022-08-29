from django.db import models

# Create your models here.
# class Post will be the name of table in database

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField(default='defaultuser@gmail.com')
    adress = models.CharField(max_length=200, blank=True)
    time_post = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{}".format(self.title)