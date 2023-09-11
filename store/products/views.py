from django.shortcuts import render

# Create your views here.

def index(request):
    data = {'title': 'INDEX', 'message': 'HELLO блин WORLD!'}
    return render(request, 'products/index.html', context=data)

def products(request):
    return render(request, 'products/products.html')
