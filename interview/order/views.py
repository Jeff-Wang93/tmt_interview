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


class OrderGetTagsView(generics.ListCreateAPIView):
    """
    example call: /orders/get-tags?id=1
    """
    queryset = Order.objects.all()
    serializer_class = OrderTagSerializer

    def get(self, request):
        order_number = request.query_params.get('id', None)
        order = self.queryset.get(id=order_number)
        order_tags = order.tags.all()

        serializer = self.serializer_class(order_tags, many=True)

        return Response(serializer.data, status=200)
