from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Удаление старых данных..."))

        # Удаление всех продуктов и категорий
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Старые данные удалены."))
        self.stdout.write("Добавление тестовых продуктов...")

        category, _ = Category.objects.get_or_create(name="Категория", description="Новая категория")

        products = [
            {"name": "Продукт 1", "description": "Новый продукт 1", "category": category, "price": 10000},
            {"name": "Продукт 2", "description": "Новый продукт 2", "category": category, "price": 20000},
            {"name": "Продукт 3", "description": "Новый продукт 3", "category": category, "price": 30000},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added product: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Product already exists: {product.name}"))
