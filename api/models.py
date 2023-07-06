from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(max_length=30)
    website = models.URLField(max_length=60)
    photo = models.ImageField(upload_to='author')
    about = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name



