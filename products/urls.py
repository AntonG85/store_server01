from django.urls import path

from products.views import index, product, products

# from views import index, products, product

app_name = 'products'

urlpatterns = [

    path('', products, name='index'),
    path('<slug:product_slug>', product, name='product'),
    ]