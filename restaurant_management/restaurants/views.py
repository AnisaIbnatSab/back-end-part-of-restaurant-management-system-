from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnerOrEmployee
from .models import Restaurant, Menu, MenuItem
from .serializers import RestaurantSerializer, MenuSerializer, MenuItemSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEmployee]

    def get_queryset(self):
        # Only return restaurants owned by the authenticated user
        return self.queryset.filter(owner=self.request.user)

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEmployee]

    def get_queryset(self):
        # Only return menus for the specified restaurant owned by the authenticated user
        return self.queryset.filter(restaurant__owner=self.request.user)

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEmployee]

    def get_queryset(self):
        # Only return menu items for menus belonging to the authenticated user's restaurant
        return self.queryset.filter(menu__restaurant__owner=self.request.user)
