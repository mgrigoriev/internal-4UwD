from django.contrib.auth.models import AbstractUser
from django.db import models

class Department(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Position(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class User(AbstractUser):
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
