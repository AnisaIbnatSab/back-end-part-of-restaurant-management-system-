from rest_framework import serializers
from .models import Order, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'status']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'menu_item', 'quantity', 'price']
