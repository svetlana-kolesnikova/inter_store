from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Contact


def home(request):
    """Контроллер страницы Home"""
    # Получаем последние 5 продуктов
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Выводим в консоль последние 5 продуктов
    print("Последние добавленные продукты:")
    for p in latest_products:
        print(p.name, p.price)

    return render(request, 'catalog/home.html', {'latest_products': latest_products})


def contacts(request):
    """Контроллер страницы Contacts"""
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т.д.)
        # Создается объект Contact
        Contact.objects.create(name=name, phone=phone, message=message)
        print(name)
        print(phone)
        print(message)

        # Возвращается простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')