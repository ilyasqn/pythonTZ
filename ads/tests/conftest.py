import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from ads.models.ads import Ad


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="pass123")


@pytest.fixture
def second_user(db):
    return User.objects.create_user(username="otheruser", password="pass123")


@pytest.fixture
def auth_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def ad_sender(second_user):
    return Ad.objects.create(
        user=second_user,
        title="Товар от второго юзера",
        description="Описание",
        category="Разное",
        condition="used"
    )


@pytest.fixture
def ad_receiver(user):
    return Ad.objects.create(
        user=user,
        title="Товар от первого юзера",
        description="Описание",
        category="Техника",
        condition="new"
    )
