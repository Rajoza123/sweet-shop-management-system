import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from sweets.models import Sweet

@pytest.mark.django_db
class TestSweetListFilter:

    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("sweet-list")

        Sweet.objects.create(
            name="Gulab Jamun",
            category="Traditional",
            price=50,
            quantity=10
        )

        Sweet.objects.create(
            name="Chocolate Cake",
            category="Modern",
            price=150,
            quantity=5
        )

    def test_list_sweets_price_less_than_100(self):
        response = self.client.get(self.url, {"max_price": 100})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert float(response.data[0]["price"]) < 100
