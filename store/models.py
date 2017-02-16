from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name;

class Product(models.Model):
    name = models.CharField(max_length =32);
    description = models.TextField();
    category = models.OneToOneField(Category);


    def __str__(self):
        return self.name;