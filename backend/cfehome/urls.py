from django.contrib import admin
from django.urls import path, include

from .routers import product_detail_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/search/', include('search.urls')),
    path('api/products/', include('products.urls')),
    path('api/v2/', include('cfehome.routers')),
    path('api/v2/<int:pk>/', product_detail_view)

]
