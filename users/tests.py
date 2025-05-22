import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestUserAPI:

    def setup_method(self):
        self.client = APIClient()

    def test_register_user_success(self):
        payload = {
            "username": "newuser",
            "password": "strongpassword123"
        }

        response = self.client.post("/api/users/register/", data=payload)

        assert response.status_code == 201
        assert User.objects.filter(username="newuser").exists()

        user = User.objects.get(username="newuser")
        assert user.check_password("strongpassword123")

    def test_register_user_missing_fields(self):
        response = self.client.post("/api/users/register/", data={})
        assert response.status_code == 400
        assert "username" in response.data
        assert "password" in response.data
