from django.test import TestCase
from django.urls import reverse
# from unittest import TestCase
from users.models import User
from products.models import Product, ProductCategory
from http import HTTPStatus


class IndexViewTestCase(TestCase):
    fixtures = ['category.json', 'goods.json']

    def setUp(self):
        self.products = Product.objects.all()
        self.category = ProductCategory.objects.all()

    def _commons(self, response, title, templ_name):
        self.assertEqual(response.context_data['title'], title)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, templ_name)

    def test_index_view(self):
        path = reverse('index')
        response = self.client.get(path)
        self._commons(response, 'STORE', 'products/index.html')

    def test_products_view(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._commons(response, 'Продукты', 'products/products.html')
        self.assertEqual(list(response.context_data['object_list']), list(self.products[:2]))

    def test_products_view_by_cattegory(self):

        path = reverse('products:category', kwargs={'category_id': self.category[0].id})
        response = self.client.get(path)

        # print(category)
        # print(list(response.context_data['object_list']))
        # print(list(products.filter(category_id=category.id)))

        self._commons(response, 'Продукты', 'products/products.html')
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products.filter(category_id=self.category[0].id)[:2]),
        )
