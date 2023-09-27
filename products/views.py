from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from store.wsgi import *
from products.models import ProductCategory, Product, Basket
from users.models import User
from slugify import slugify
from django.contrib.auth.decorators import login_required

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

