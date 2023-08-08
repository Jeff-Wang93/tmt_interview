from django.shortcuts import render
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderDeactivateView(generics.ListCreateAPIView):
    """
    example call: /orders/deactivate?id=1

    I made them get calls so it's easy to just use the browser and see it working rather than
    pulling out postman or something similar to make a POST/PATCH call
    """
    from interview.order.serializers import OrderIsActiveSerializer
    queryset = Order.objects.all()
    serializer_class = OrderIsActiveSerializer

    def get(self, request, *args, **kwargs):
        from rest_framework.response import Response
        from interview.order.serializers import OrderIsActiveSerializer

        order_number = request.query_params.get('id', None)
        order = self.queryset.get(id=order_number)

        order.is_active = False
        order.save()

        serializer = self.serializer_class(order)
        return Response(serializer.data, status=200)

