from django.contrib import admin
from django.urls import path
from products.views import ProductsView, ProductsIdFnView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductsView.as_view(), name='products_save_getall'),
    path('products/<int:id>/', ProductsIdFnView.as_view(), name='products_id_fn')
]
