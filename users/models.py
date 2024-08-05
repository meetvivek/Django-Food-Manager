from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    
    image = models.ImageField(default="profile.jpg", upload_to="Profile_Pictures")
    full_name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pin_code = models.CharField(max_length=10, blank=True)
    favorite_food = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

