from rest_framework import serializers
from .models import Restaurant, Menu, MenuItem

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'location', 'created_at']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'name', 'created_at']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'menu', 'name', 'price', 'description', 'available']
