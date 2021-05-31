from django.db import models

# Create your models here.

# The first step is to create a model


class student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=10)
    section = models.CharField(max_length=20)

    def __str__(self):
        return self.name
