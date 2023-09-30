from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from store.wsgi import *
from products.models import ProductCategory, Product, Basket
from users.models import User
from slugify import slugify
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    context = {'title': 'START PAGE', 'message': 'HELLO WORLD!'}
    return render(request, 'products/index.html', context)

def products(request, category_id=None, page_number=1):

    # for prod in Product.objects.all():
    #     prod.slug = slugify(prod.name)
    #     prod.save()
    # for prod in ProductCategory.objects.all():
    #     prod.slug = slugify(prod.name)
    #     prod.save()

    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 2
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title' : 'Продукты',
        'products' : products_paginator,
        'categorys' : ProductCategory.objects.all(),
        'cat_id': category_id,
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

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.last()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])

@login_required
def basket_remove (request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])

