from django.shortcuts import render, get_object_or_404
from store.wsgi import *
from products.models import ProductCategory, Product
from slugify import slugify

# Create your views here.

def index(request):
    context = {'title': 'START PAGE', 'message': 'HELLO WORLD!'}
    return render(request, 'products/index.html', context)

def products(request):

    # for prod in Product.objects.all():
    #     prod.slug = slugify(prod.name)
    #     prod.save()
    #
    # for prod in ProductCategory.objects.all():
    #     prod.slug = slugify(prod.name)
    #     prod.save()

    context = {
        'title' : 'Продукты',
        'products' : Product.objects.all(),
        'categorys' : ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)

def product(request, product_slug: str):

    prod = get_object_or_404(Product, slug=product_slug)

    context = {
        'title' : prod.slug,
        'product' : prod,
        'categorys' : ProductCategory.objects.all(),
    }
    return render(request, 'products/product_desc.html', context)
