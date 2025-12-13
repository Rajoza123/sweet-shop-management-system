from rest_framework import serializers
from .models import Sweet

class SweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweet
        fields = ["id", "name", "category", "price", "quantity"]

    def validate_name(self, value):
        if Sweet.objects.filter(name=value).exists():
            raise serializers.ValidationError("Sweet with this name already exists")
        return value
