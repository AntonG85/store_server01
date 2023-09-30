from django.urls import path

from products.views import index, product, products, basket_add, basket_remove

# from views import index, products, product

app_name = 'products'

urlpatterns = [

    path('<slug:product_slug>', product, name='product'),
    path('', products, name='index'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page_number>', products, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    ]