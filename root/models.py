from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ability(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Score(models.Model):
    count = models.IntegerField(default=5)

    def __str__(self):
        return str(self.count)
    
class Testimonials(models.Model):
    title = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="tester", default="default.jpg")
    content = models.TextField()
    domain = models.CharField(max_length=30)
    stars = models.ForeignKey(Score, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
    def stars_count(self):
        return range(self.stars.count)


class Agents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="agent", default="default.jpg")
    twitter = models.CharField(max_length=220)
    instagram = models.CharField(max_length=220)
    facebook = models.CharField(max_length=220)
    linkedin = models.CharField(max_length=220)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.user.first_name


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    
