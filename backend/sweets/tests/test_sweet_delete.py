import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from sweets.models import Sweet

User = get_user_model()


@pytest.mark.django_db
class TestSweetDeleteAPI:

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
            name="Ladoo",
            category="Traditional",
            price=10.00,
            quantity=20
        )

        self.url = reverse("sweet-delete", kwargs={"pk": self.sweet.id})

    def test_admin_can_delete_sweet(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.delete(self.url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Sweet.objects.filter(id=self.sweet.id).count() == 0

    def test_non_admin_forbidden(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(self.url)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_unauthenticated_user(self):
        response = self.client.delete(self.url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_non_existing_sweet(self):
        self.client.force_authenticate(user=self.admin)

        url = reverse("sweet-delete", kwargs={"pk": 999})

        response = self.client.delete(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
