from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from .models import Sweet


@transaction.atomic
def purchase_sweet(sweet_id):
    sweet = Sweet.objects.select_for_update().filter(id=sweet_id).first()

    if not sweet:
        raise Sweet.DoesNotExist

    if sweet.quantity <= 0:
        raise ValidationError("Out of stock")

    sweet.quantity -= 1
    sweet.save()

    return sweet
