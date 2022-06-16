import imp
from rest_framework import generics, mixins
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.mixins import StaffEditorPermissionMixin

class ProductListCreateView(
             StaffEditorPermissionMixin,
           generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     CustomTokenAuthentication
    # ]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        serializer.save()
        # send a django signal or add serializer.save(suer=serlf.request.user)


class ProductDestroyAPIView(generics.DestroyAPIView,
                        StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)

class ProductUpdateAPIView(generics.UpdateAPIView,
                        StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDetailAPIView(generics.RetrieveAPIView,
                            StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'



class ProductListAPIView(generics.ListAPIView):
    """
        not gonna use this method
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    """
        not gonna use this method
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        serializer.save()
        # send a django signal or add serializer.save(suer=serlf.request.user)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'



#### not gonna use


class ProductMixinView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lockup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)


@api_view(['GET', "POST"])
def product_alt(request, pk=None, *args, **kwargs):
    method = request

    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)  # http 404
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # url args
        #  get request -> detail view
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == 'POST':
        pass


