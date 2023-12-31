from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from products.models import Basket, Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'STORE'


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 2
    title = 'Продукты'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context.update({
            'cat_id': self.kwargs.get('category_id'),
            'categorys': ProductCategory.objects.all(),
            })
        return context


def product(request, product_slug: str):
    prod = get_object_or_404(Product, slug=product_slug)

    context = {
        'title': prod.slug,
        'product': prod,
        'categorys': ProductCategory.objects.all(),
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
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(redirect_to=request.META['HTTP_REFERER'])
