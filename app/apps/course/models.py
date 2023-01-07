from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

