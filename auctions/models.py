from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.AutoField(primary_key=True)

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    price = models.IntegerField()
    image = models.CharField(max_length=128, blank=True)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name="userListing")

    def __str__(self):
        return f"{self.title} is priced at ({self.price})"

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userBid")
    currentListing = models.ManyToManyField(Listing, related_name="bidListing")

    def __str__(self):
        return f"{self.user} bid {self.price} on {self.currentListing}"

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(User, blank=True, related_name="userComment")
    content = models.CharField(max_length=128)
    currentListing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="commentListing")

    def __str__(self):
        return f"{self.user} commented {self.content} on {self.currentListing}"

class WatchList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userID")
    currentListing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchListing")