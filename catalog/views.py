from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .services import get_products_by_category
from .forms import ProductForm
from .models import Contact, Product, Category


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
        # пробуем получить из кэша
        products = cache.get("products_list")

        # если нет — берём из БД
        if not products:
            products = Product.objects.order_by("-created_at")
            # кладём в кеш на 5 минут (можно изменить)
            cache.set("products_list", products, 60 * 5)

        return products


@method_decorator(cache_page(60 * 5), name='dispatch')   # кэш на 5 минут
class ProductDetailView(LoginRequiredMixin, DetailView):
    """Детали конкретного продукта"""

    model = Product
    template_name = "catalog/product_details.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Добавление нового продукта"""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def get_success_url(self):
        return reverse("catalog:product_details", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.save()

        #  очищаем кеш списка
        cache.delete("products_list")

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Добавление нового продукта"""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    #  проверка: редактировать может только владелец
    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user:
            return HttpResponseForbidden("Вы не можете редактировать чужой продукт!")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)

        #  удаляем кеш списка
        cache.delete("products_list")

        return response

    def get_success_url(self):
        return reverse("catalog:product_details", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление продукта"""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")

    #  удалять может владелец или модератор
    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        # владелец — можно
        if product.owner == request.user:
            return super().dispatch(request, *args, **kwargs)

        # модератор продуктов — тоже можно
        if request.user.has_perm("catalog.delete_product"):
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseForbidden("У вас нет прав на удаление этого продукта.")

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)

        #  очищаем кеш списка
        cache.delete("products_list")

        return response


class UnpublishProductView(LoginRequiredMixin, View):
    """Отмена публикации продукта"""

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав для отмены публикации продукта.")

        # Логика статуса публикации книги
        product.is_published = False
        product.save()

        return redirect("catalog:product_details", pk=pk)


class ProductsByCategoryView(ListView):
    template_name = "catalog/products_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs["category_id"]
        context["category"] = Category.objects.get(pk=category_id)
        return context