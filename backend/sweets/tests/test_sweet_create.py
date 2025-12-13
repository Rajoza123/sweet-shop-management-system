import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestSweetCreateAPI:

    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("sweet-create")

        # Admin user
        self.admin = User.objects.create_user(
            username="admin",
            email="admin@example.com",
            password="AdminPass123!",
            is_staff=True
        )

        # Normal user
        self.user = User.objects.create_user(
            username="raj",
            email="raj@example.com",
            password="Pass1234!",
            is_staff=False
        )

    def test_create_sweet_success(self):
        """Admin creates a sweet successfully."""
        payload = {
            "name": "Gulab Jamun",
            "category": "Traditional",
            "price": 20.5,
            "quantity": 50
        }

        # Authenticate as admin
        self.client.force_authenticate(user=self.admin)

        response = self.client.post(self.url, payload, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["name"] == payload["name"]
        assert response.data["category"] == payload["category"]
        assert response.data["price"] == payload["price"]
        assert response.data["quantity"] == payload["quantity"]

    def test_create_sweet_non_admin_forbidden(self):
        """Normal user should NOT be able to create sweets."""
        payload = {
            "name": "Barfi",
            "category": "Traditional",
            "price": 30,
            "quantity": 100
        }

        # Authenticate as normal user
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.url, payload, format="json")

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "detail" in response.data

    def test_create_sweet_duplicate_name(self):
        """Sweet name must be unique."""
        self.client.force_authenticate(user=self.admin)

        payload = {
            "name": "Barfi",
            "category": "Traditional",
            "price": 30,
            "quantity": 50
        }

        # First create sweet
        self.client.post(self.url, payload, format="json")

        # Attempt duplicate
        response = self.client.post(self.url, payload, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "name" in response.data
