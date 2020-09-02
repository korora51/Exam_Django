from django.db import models
from datetime import datetime
class Offer(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField(blank=True)
    photo_prem = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    photo1 = models.ImageField(upload_to="uploads/%Y/%m/%d/", blank=True)
    photo2 = models.ImageField(upload_to="uploads/%Y/%m/%d/", blank=True)
    photo3 = models.ImageField(upload_to="uploads/%Y/%m/%d/", blank=True)
    price = models.IntegerField("Price-tag")

    def __str__(self):
        return self.name

