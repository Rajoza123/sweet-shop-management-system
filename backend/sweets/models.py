from django.db import models
from django.core.exceptions import ValidationError

class Sweet(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def clean(self):
        if self.price <= 0:
            raise ValidationError({"price": "Price must be positive"})
