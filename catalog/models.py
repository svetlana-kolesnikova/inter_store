from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория', help_text='Введите название категории')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание породы', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование', help_text='Введите название продукта')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Изображение',
                              help_text='Загрузате фото продукта')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', help_text='Введите цену товара')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
