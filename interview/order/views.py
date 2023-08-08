from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrdersWithTagView(generics.ListCreateAPIView):
    """
    example call: /orders/with-tag/?tag=Dubbing
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        tag = request.query_params.get('tag', None)

        order_tag = OrderTag.objects.get(name=tag)

        orders = self.queryset.filter(tags=order_tag)
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data, status=200)
