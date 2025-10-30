from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductForm
from .models import Contact, Product


class HomeView(ListView):
    """Страница Home: вывод последних 5 продуктов"""

    model = Product
    template_name = "catalog/home.html"
    context_object_name = "latest_products"

    def get_queryset(self):
        return Product.objects.order_by("-created_at")[:5]


class ContactsView(View):
    """Страница Contacts — обработка формы обратной связи"""

    template_name = "catalog/contacts.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        Contact.objects.create(name=name, phone=phone, message=message)

        print(name, phone, message)
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductListView(ListView):
    """Список всех продуктов"""

    model = Product
    template_name = "catalog/products_list.html"
    context_object_name = "products"
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.order_by("-created_at")


class ProductDetailView(DetailView):
    """Детали конкретного продукта"""

    model = Product
    template_name = "catalog/product_details.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    """Добавление нового продукта"""

    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"

    def get_success_url(self):
        return reverse("catalog:product_details", kwargs={"pk": self.object.pk})


class ProductUpdateView(UpdateView):
    """Добавление нового продукта"""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def get_success_url(self):
        return reverse("catalog:product_details", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    """Удаление продукта"""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")
