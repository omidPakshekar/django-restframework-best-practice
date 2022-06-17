from rest_framework import serializers

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        print(obj)
        user = obj 
        my_products = user.product_set.all()
        return []



