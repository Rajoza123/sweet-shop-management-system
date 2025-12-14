import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from sweets.models import Sweet

User = get_user_model()


@pytest.mark.django_db
class TestSweetUpdateAPI:

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
            quantity=50
        )

        self.url = reverse("sweet-update", kwargs={"pk": self.sweet.id})

    def test_admin_can_update_sweet(self):
        self.client.force_authenticate(user=self.admin)

        payload = {
            "name": "Milk Barfi",
            "category": "Traditional",
            "price": 35.00,
            "quantity": 40
        }

        response = self.client.put(self.url, payload, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == "Milk Barfi"
        assert float(response.data["price"]) == 35.0
        assert response.data["quantity"] == 40

    def test_non_admin_forbidden(self):
        self.client.force_authenticate(user=self.user)

        payload = {
            "name": "Bad Update"
        }

        response = self.client.put(self.url, payload, format="json")

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_invalid_sweet(self):
        self.client.force_authenticate(user=self.admin)

        url = reverse("sweet-update", kwargs={"pk": 999})

        response = self.client.put(
            url,
            {"name": "Does not exist"},
            format="json"
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_invalid_data(self):
        self.client.force_authenticate(user=self.admin)

        payload = {
            "price": -10
        }

        response = self.client.put(self.url, payload, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_update_unauthenticated(self):
        payload = {
            "name": "Unauth Update"
        }

        response = self.client.put(self.url, payload, format="json")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
