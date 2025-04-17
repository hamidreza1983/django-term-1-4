from django.test import TestCase, Client
from .forms import CommentForm
from .models import Services
from accounts.models import User




# class TestForm(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(email="user@test.com", password="H@midreza62")
    
#     def test_form_comment(self):
#         user = self.user
#         service = Services.objects.create(
#             title="test",
#             agent = "<create an object of agent>",


#         )
#         """form = CommentForm(data={
#             "name" : obj user,...
#         })"""
#         self.assertTrue()

