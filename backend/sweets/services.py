from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError

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

@transaction.atomic
def restock_sweet(sweet_id, amount):
    sweet = Sweet.objects.select_for_update().filter(id=sweet_id).first()

    if not sweet:
        raise Sweet.DoesNotExist

    if amount <= 0:
        raise ValidationError("Amount must be greater than zero")

    sweet.quantity += amount
    sweet.save()

    return sweet

@transaction.atomic
def update_sweet(sweet_id, data):
    sweet = Sweet.objects.select_for_update().filter(id=sweet_id).first()

    if not sweet:
        raise Sweet.DoesNotExist

    for field in ["name", "category", "price", "quantity"]:
        if field in data:
            setattr(sweet, field, data[field])

    try:
        sweet.full_clean()
    except DjangoValidationError as e:
        raise DRFValidationError(e.message_dict)

    sweet.save()
    return sweet