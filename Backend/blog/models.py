from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import CITextField
# Create your models here.

class Category(models.Model):
    name = CITextField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return self.title

