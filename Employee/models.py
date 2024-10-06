from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name