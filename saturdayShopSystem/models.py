from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    qtty = models.CharField(max_length=15, blank=False, null=False)
    price = models.CharField(max_length=10, blank=False, null=False)
    description = models.CharField(max_length=400, blank=False, null=False)


def __str__(self):
    return self.name