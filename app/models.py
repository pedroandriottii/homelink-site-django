from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_description = models.CharField(max_length=260, null=True, blank=True)

    def __str__(self):
        return self.title
