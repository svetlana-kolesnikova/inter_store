from django.core.cache import cache
from django.views.decorators.cache import cache_page

from config import settings

from .models import Product


def get_products_by_category(category_id):
    """Возвращает список опубликованных продуктов по категории"""
    return Product.objects.filter(category_id=category_id, is_published=True)


def get_cached_products():
    """Кеширование списка продуктов"""
    if not settings.CACHE_ENABLED:
        # если кеш выключен — возвращаем данные напрямую
        return Product.objects.order_by("-created_at")

    key = "products_list"
    products = cache.get(key)

    if products is None:
        products = list(Product.objects.order_by("-created_at"))
        cache.set(key, products, 60 * 5)  # кэш на 15 минут

    return products


def conditional_cache_page(timeout):
    """Оборачиваем декоратор в условие для отключения кеширования"""

    if settings.CACHE_ENABLED:
        return cache_page(timeout)
    return lambda func: func
