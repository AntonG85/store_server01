from django.contrib import admin

from products.models import ProductCategory, Product, Basket

# admin.site.register(Product)
# admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    fields = ['name', 'category', ('price', 'quantity'),  'description', 'image', 'slug']
    readonly_fields = ['slug']
    search_fields = ['name']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['slug']

# @admin.register(Basket)
# class BasketAdmin(admin.ModelAdmin):
#     list_display = ['user', 'product', 'quantity']
#     ordering = ['user']


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'created_timestamp']
    readonly_fields = ['created_timestamp']
    extra = 0
