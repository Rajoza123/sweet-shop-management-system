import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from sweets.models import Sweet

User = get_user_model()


@pytest.mark.django_db
class TestSweetRestockAPI:

    def setup_method(self):
        self.client = APIClient()

        self.admin = User.objects.create_user(
            username="admin",
            email="admin@example.com",
            password="AdminPass123!",
            is_staff=True
        )

        self.user = User.objects.create_user(
            username="raj",
            email="raj@example.com",
            password="Pass1234!",
            is_staff=False
        )

        self.sweet = Sweet.objects.create(
            name="Barfi",
            category="Traditional",
            price=30.00,
            quantity=10
        )

        self.url = reverse("sweet-restock", kwargs={"pk": self.sweet.id})

    def test_admin_can_restock(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.post(
            self.url,
            {"amount": 20},
            format="json"
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["quantity"] == 30

    def test_non_admin_forbidden(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(
            self.url,
            {"amount": 10},
            format="json"
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_invalid_amount(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.post(
            self.url,
            {"amount": -5},
            format="json"
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "detail" in response.data

    def test_invalid_sweet(self):
        self.client.force_authenticate(user=self.admin)

        url = reverse("sweet-restock", kwargs={"pk": 999})

        response = self.client.post(
            url,
            {"amount": 10},
            format="json"
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
