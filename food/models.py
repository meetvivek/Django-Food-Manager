from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://play-lh.googleusercontent.com/JA0qswBq-iSo5HbTZyyqAEYEdQ-9JjmkNqxyCqAndO8JzHwKnRSzcGrKdhrshDxw4w=w480-h960-rw")