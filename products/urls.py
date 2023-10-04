from django.urls import path

from products.views import product, basket_add, basket_remove, ProductsListView


app_name = 'products'

urlpatterns = [

    path('<slug:product_slug>', product, name='product'),
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>', ProductsListView.as_view(), name='category'),
    # path('page/<int:page_number>', ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    ]