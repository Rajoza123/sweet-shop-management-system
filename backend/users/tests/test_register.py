import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestRegisterAPI:

    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("register")

    def test_register_success(self):
        payload = {
            "username": "raj",
            "email": "raj@example.com",
            "password": "Pass1234!"
        }

        response = self.client.post(self.url, payload, format="json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["username"] == payload["username"]
        assert response.data["email"] == payload["email"]

        user_exists = User.objects.filter(username="raj").exists()
        assert user_exists is True

    def test_register_duplicate_username(self):
        User.objects.create_user(
            username="raj",
            email="old@example.com",
            password="oldpass123"
        )

        payload = {
            "username": "raj",
            "email": "raj@example.com",
            "password": "Pass1234!"
        }

        response = self.client.post(self.url, payload, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "username" in response.data or "detail" in response.data

    def test_register_invalid_password(self):
        payload = {
            "username": "raj2",
            "email": "raj2@example.com",
            "password": "123"  # invalid
        }

        response = self.client.post(self.url, payload, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST
