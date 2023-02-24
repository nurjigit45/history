# from abc import ABCMeta
from rest_framework import serializers
from .models import Product


class Product_serializer_list(serializers.Serializer):

    class meta:
        models = Product
        fields = '__all__'



class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    text = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True, min_value=1, max_value=1000000)
    quantity = serializers.IntegerField(required=True, min_value=1, max_value=10)
    size = serializers.FloatField(required=True, min_value=1, max_value=100)
    color = serializers.IntegerField(required=True)










