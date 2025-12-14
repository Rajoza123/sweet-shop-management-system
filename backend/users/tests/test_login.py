import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestLoginAPI:

    def setup_method(self):
        self.client = APIClient()
        self.url = reverse("login")

        # create a user to login with
        self.user = User.objects.create_user(
            username="raj",
            email="raj@example.com",
            password="Pass1234!"
        )

    def test_login_success(self):
        payload = {
            "username": "raj",
            "password": "Pass1234!"
        }

        response = self.client.post(self.url, payload, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data

    def test_login_invalid_credentials(self):
        payload = {
            "username": "raj",
            "password": "WrongPass"
        }

        response = self.client.post(self.url, payload, format="json")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "detail" in response.data
