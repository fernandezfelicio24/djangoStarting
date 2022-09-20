from django.db import models
from django.utils.text import slugify
# Create your models here.
# class Post will be the name of table in database

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField(default='defaultuser@gmail.com')
    adress = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=255, default='Science')
    slug = models.SlugField(blank=True, editable=False)
    time_post = models.DateTimeField(auto_now_add=True)

    def save(self,  *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return "{} . {}".format(self.id, self.title)