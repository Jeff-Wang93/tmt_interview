
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrdersWithTagView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('with-tag/', OrdersWithTagView.as_view(), name='orders-with-tag'),
]
