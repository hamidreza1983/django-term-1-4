import pytest
from rest_framework.test import APIClient




@pytest.fixture
def client_api():
    client = APIClient()
    return client


@pytest.mark.django_db
class TestServices:

    def test_response (self, client_api):
        url = "http://127.0.0.1:8000/services/api/v1/services/"
        res = client_api.get(url)
        assert (res.status_code == 200)


