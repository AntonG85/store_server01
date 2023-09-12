from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'title': 'START PAGE', 'message': 'HELLO блин WORLD!'}
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'products' : [
            { 'name' : 'Худи черного цвета с монограммами adidas Originals',
            'image' : '/static/vendor/img/products/Adidas-hoodie.png',
            'price' : 6090,
            'description' : 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', },

            { 'name' : 'Синяя куртка The North Face',
            'image' : '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
            'price' : 23725,
            'description' : 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.', },

            { 'name' : 'Черный рюкзак Nike Heritage',
            'image' : '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
            'price' : 2340,
            'description' : 'Плотная ткань. Легкий материал.', },

            { 'name' : 'Коричневый спортивный oversized-топ ASOS DESIGN',
            'image' : '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
            'price' : 3390,
            'description' : 'Материал с плюшевой текстурой. Удобный и мягкий.', },
                    ],
    }
    return render(request, 'products/products.html', context)
