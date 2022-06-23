from turtle import title
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title, unique_product_title

from api.serializer import UserPublicSerializer
from api.serializer import ProductInlineSerializer

class ProductSerializer(serializers.ModelSerializer):
    # owner = UserPublicSerializer(source='user', read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail-api',
        lookup_field='pk'
    )
    email = serializers.EmailField( write_only=True)
    # email = serializers.EmailField(source='user.email', read_only=True)
    title = serializers.CharField(validators=[unique_product_title])
    # related_products = ProductInlineSerializer(source='user.product_set.all', many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            # 'owner',
            'email',
            'url',
            'edit_url',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            # 'related_products',
            'public',
            'path',
            'endpoint',
        ]

    # def validate_title(self, value):
    #     # iexact --> case sensetive and exact --> non case sensetive
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is duplicate")
    #     return value

    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title')
    #     return instance

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('product-update-api', kwargs={'pk' : obj.pk}, request=request)
 
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
