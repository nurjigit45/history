from django.urls import path
from product.views import ProductsListAPIView

urlpatterns = [
    path('product/', ProductsListAPIView),
]













