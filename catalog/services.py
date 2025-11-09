from .models import Product
from django.core.cache import cache


def get_products_by_category(category_id):
    """Возвращает список опубликованных продуктов по категории"""
    return Product.objects.filter(category_id=category_id, is_published=True)


def get_cached_products():
    key = "product_list"
    products = cache.get(key)

    if products is None:
        products = Product.objects.all()
        cache.set(key, products, 60)  # кэш на 60 секунд

    return products