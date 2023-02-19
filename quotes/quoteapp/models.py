from django.views.generic import ListView

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['id']


class Author(models.Model):
    fullname = models.CharField(max_length=100, null=True, unique=True)
    born_date = models.DateField(null=True, unique=True)
    born_location = models.CharField(max_length=100, null=True, unique=True)
    description = models.CharField(max_length=5000, null=True, unique=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):
    quote = models.CharField(max_length=2500, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='tags')

    def __str__(self):
        return f"{self.quote}"

    class Meta:
        ordering = ['id']
