from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='product_create_api'),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product_detail_api'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product_update_api'),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view(), name='product_delete_api'),


]
