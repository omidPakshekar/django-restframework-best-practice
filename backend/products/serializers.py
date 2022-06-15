from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]




    # if we dont save serializer and write serializer.data
    def get_my_discount(self, obj):
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    # def get_my_discount(self, obj):
    #     try:
    #         print('def get_my_discount --> title', obj.title)
    #         return obj.get_discount()
    #     except Exception as e:
    #         return None



    # def get_my_discount(self, obj):
    #     print('def get_my_discount --> title', obj.title)
    #     return obj.get_discount()
