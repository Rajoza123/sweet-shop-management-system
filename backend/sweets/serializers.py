from rest_framework import serializers
from .models import Sweet

class SweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sweet
        fields = ["id", "name", "category", "price", "quantity"]
        extra_kwargs = {
            "name": {"validators": []},  # disable default UniqueValidator
        }

    def validate_name(self, value):
        if Sweet.objects.filter(name=value).exists():
            raise serializers.ValidationError("Sweet with this name already exists")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be positive")
        return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative")
        return value
