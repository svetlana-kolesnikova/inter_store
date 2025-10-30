from django import forms
from django.core.exceptions import ValidationError
from PIL import Image  # Pillow нужен для проверки формата

from .constants import ALLOWED_FORMATS, FORBIDDEN_WORDS, MAX_IMAGE_SIZE_MB
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите название продукта",  # Текст подсказки внутри поля
            }
        )

        # Настройка атрибутов виджета для поля 'description'
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите описание продукта",  # Текст подсказки внутри поля
            }
        )

        # Настройка атрибутов виджета для поля 'category'
        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Выберите категорию",  # Текст подсказки внутри поля
            }
        )

        # Настройка атрибутов виджета для поля 'image'
        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Добавить изображение",  # Текст подсказки внутри поля
            }
        )

        # Настройка атрибутов виджета для поля 'price'
        self.fields["price"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите цену продукта",  # Текст подсказки внутри поля
            }
        )

        # Стилизация булевого поля
        if "is_active" in self.fields:
            self.fields["is_active"].widget = forms.CheckboxInput(attrs={"class": "form-check-input"})

    def clean_price(self):
        """Проверка цены на наличие и на положительный признак"""
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной")
        return price

    def clean(self):
        """Проверка названия и описания продукта на наличие запрещённых слов"""
        cleaned_data = super().clean()
        name = cleaned_data.get("name", "").lower()
        description = cleaned_data.get("description", "").lower()

        for word in FORBIDDEN_WORDS:
            if word in name:
                self.add_error("name", f"Название содержит запрещённое слово: {word}")
            if word in description:
                self.add_error("description", f"Описание содержит запрещённое слово: {word}")

        return cleaned_data

    def clean_image(self):
        """Проверка изображения по критериям"""
        image = self.cleaned_data.get("image")

        if not image:
            return image  # Поле может быть пустым, если не обязательно

        # Проверка размера
        if image.size > MAX_IMAGE_SIZE_MB * 1024 * 1024:
            raise ValidationError(f"Размер изображения не должен превышать {MAX_IMAGE_SIZE_MB} МБ")

        # Проверка формата
        try:
            img = Image.open(image)
            if img.format not in ALLOWED_FORMATS:
                raise ValidationError("Допустимые форматы изображения: JPEG или PNG")
        except Exception:
            raise ValidationError("Невозможно прочитать изображение. Загрузите корректный файл")

        return image
