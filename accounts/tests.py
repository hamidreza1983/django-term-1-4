from django.test import TestCase
from .models import User



class TestCreateUser(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            email="user@test.com",
            password="H@midreza62"
        )
        self.assertEqual(user.email, "user@test.com")

# Create your tests here.
