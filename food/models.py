from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200, blank=False)
    item_desc = models.CharField(max_length=500, blank=False)
    item_price = models.IntegerField(blank=False)
    item_image = models.CharField(max_length=500, default="https://play-lh.googleusercontent.com/JA0qswBq-iSo5HbTZyyqAEYEdQ-9JjmkNqxyCqAndO8JzHwKnRSzcGrKdhrshDxw4w=w480-h960-rw")

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})