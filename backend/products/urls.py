from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='product-create-api'),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail-api'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-update-api'),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view(), name='product-delete-api'),


]
