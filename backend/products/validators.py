from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Product


def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name.")
    return value


#  another way to choose unique
unique_product_title = UniqueValidator(queryset=Product.objects.all(),
                                        lookup="iexact")