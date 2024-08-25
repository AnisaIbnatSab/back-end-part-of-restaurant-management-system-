import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class StripePaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.data.get('stripeToken')
        try:
            charge = stripe.Charge.create(
                amount=5000,  # amount in cents
                currency='usd',
                description='Example charge',
                source=token,
            )
            return Response({'status': 'Payment successful'}, status=200)
        except stripe.error.CardError as e:
            return Response({'error': str(e)}, status=400)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return orders placed by the authenticated user
        return self.queryset.filter(user=self.request.user)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return order items for orders placed by the authenticated user
        return self.queryset.filter(order__user=self.request.user)            
