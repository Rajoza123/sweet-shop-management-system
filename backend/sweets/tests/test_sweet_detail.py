import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from sweets.models import Sweet

User = get_user_model()


@pytest.mark.django_db
class TestSweetDetailAPI:

    def setup_method(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="raj",
            email="raj@example.com",
            password="Pass1234!"
        )

        self.sweet = Sweet.objects.create(
            name="Gulab Jamun",
            category="Traditional",
            price=20.50,
            quantity=50
        )

        self.url = reverse("sweet-detail", kwargs={"pk": self.sweet.id})

    def test_get_sweet_detail_success(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == self.sweet.id
        assert response.data["name"] == "Gulab Jamun"
        assert response.data["category"] == "Traditional"
        assert float(response.data["price"]) == 20.5
        assert response.data["quantity"] == 50

    def test_get_sweet_detail_not_found(self):
        self.client.force_authenticate(user=self.user)

        url = reverse("sweet-detail", kwargs={"pk": 999})

        response = self.client.get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_get_sweet_detail_unauthenticated(self):
        response = self.client.get(self.url)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
