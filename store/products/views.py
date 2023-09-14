from django.shortcuts import render
from store.wsgi import *
from products.models import ProductCategory, Product

# Create your views here.

def index(request):
    context = {'title': 'START PAGE', 'message': 'HELLO блин WORLD!'}
    return render(request, 'products/index.html', context)

def products(request):

    context = {
        'title' : 'Продукты',
        'products' : Product.objects.all(),
        'categorys' : ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
