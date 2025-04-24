import pytest
from rest_framework.test import APIClient
from accounts.models import User

@pytest.fixture
def client_api():
    client = APIClient()
    return client


@pytest.fixture
def user():
    user = User.objects.create_user(email="user@test.com", password="H@midreza62")
    return user

@pytest.mark.django_db
class TestAuth:
    def test_view_logout(self, user, client_api):
        url="http://127.0.0.1:8000/accounts/api/v1/logout/"
        res = client_api.get(url)
        assert res.status_code == 401

    def test_view_logout_with_login(self, user, client_api):
        url="http://127.0.0.1:8000/accounts/api/v1/logout/"
        client_api.force_authenticate(user=user)
        res = client_api.post(url)
        #data = res.json()
        assert res.status_code == 204

