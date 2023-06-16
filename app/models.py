from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    name = models.CharField(max_length=200, null=True, blank=True)
    product_description = models.CharField(max_length=260, null=True, blank=True)

    def __str__(self):
        return self.title
