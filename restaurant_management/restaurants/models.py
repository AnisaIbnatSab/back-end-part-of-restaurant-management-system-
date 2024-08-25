from django.db import models
from users.models import CustomUser

class Restaurant(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
