import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from sweets.models import Sweet

User = get_user_model()


@pytest.mark.django_db
class TestSweetListAPI:

    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("sweet-list")

        # normal authenticated user
        self.user = User.objects.create_user(
            username="raj",
            email="raj@example.com",
            password="Pass1234!"
        )

        # create test sweets
        Sweet.objects.create(
            name="Gulab Jamun",
            category="Traditional",
            price=20.50,
            quantity=50
        )
        Sweet.objects.create(
            name="Barfi",
            category="Traditional",
            price=30.00,
            quantity=100
        )
        Sweet.objects.create(
            name="Chocolate Cake",
            category="Bakery",
            price=150.00,
            quantity=20
        )

        self.client.force_authenticate(user=self.user)

    def test_list_all_sweets(self):
        response = self.client.get(self.url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_filter_by_category(self):
        response = self.client.get(self.url, {"category": "Traditional"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        for sweet in response.data:
            assert sweet["category"] == "Traditional"

    def test_filter_by_min_price(self):
        response = self.client.get(self.url, {"min_price": 50})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == "Chocolate Cake"

    def test_filter_by_max_price(self):
        response = self.client.get(self.url, {"max_price": 30})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_search_by_name(self):
        response = self.client.get(self.url, {"name": "bar"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["name"] == "Barfi"
