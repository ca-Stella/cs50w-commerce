from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=8, decimal_places=2)
    url = models.ImageField()
    category = models.CharField()

    def __str__(self):
        return f"{self.title}"


class Bids(models.Model):
    pass

class Comments(models.Model):
    pass