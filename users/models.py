from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
# Create your models here.
# This is a Django model for a User. It has two fields: name and email.