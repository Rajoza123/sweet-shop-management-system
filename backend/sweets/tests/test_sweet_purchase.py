import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from sweets.models import Sweet

User = get_user_model()


@pytest.mark.django_db
class TestSweetPurchaseAPI:

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
            quantity=2
        )

        self.url = reverse("sweet-purchase", kwargs={"pk": self.sweet.id})
        self.client.force_authenticate(user=self.user)

    def test_purchase_success(self):
        response = self.client.post(self.url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["quantity"] == 1

    def test_purchase_out_of_stock(self):
        self.sweet.quantity = 0
        self.sweet.save()

        response = self.client.post(self.url)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "detail" in response.data

    def test_purchase_invalid_sweet(self):
        url = reverse("sweet-purchase", kwargs={"pk": 999})

        response = self.client.post(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
