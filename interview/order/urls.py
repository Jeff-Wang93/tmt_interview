
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderGetTagsView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('get-tags/', OrderGetTagsView.as_view(), name='order-get-tags'),
]
