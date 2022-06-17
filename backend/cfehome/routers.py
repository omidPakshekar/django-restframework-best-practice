from posixpath import basename
from django.urls import URLPattern
from rest_framework.routers import DefaultRouter

from products.viewsets import ProductGenricViewSet, ProductViewSet


router = DefaultRouter()
router.register('hi-abc', ProductViewSet, basename='products')
# print(router.urls)
urlpatterns = router.urls

product_list = ProductGenricViewSet.as_view({'get' : 'list' })
product_detail_view = ProductGenricViewSet.as_view({'get' : 'retrieve' })