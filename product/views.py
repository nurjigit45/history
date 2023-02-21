from product.models import Product
from rest_framework.generics import ListAPIView


class ProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()



