from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BlogForm
from .models import Blog


class BlogListView(ListView):
    """Список всех блоговых записей"""

    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "blogs"
    paginate_by = 6

    def get_queryset(self):
        # Отображаем только опубликованные записи
        return Blog.objects.filter(is_published=True).order_by("-created_at")


class BlogDetailView(LoginRequiredMixin, DetailView):
    """Детальный просмотр одной записи"""

    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        """Счётчик просмотров статьи"""

        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=["views_count"])

        # Проверяем достижение 100 просмотров
        if obj.views_count == 100:
            self.send_congrat_email(obj)

        return obj

    def send_congrat_email(self, blog):
        """Отправка сообщения о достижении 100 просмотров на e-mail"""

        subject = f"Блог '{blog.title}' достиг 100 просмотров!"
        message = f"Поздравляем! Ваша статья '{blog.title}' достигла 100 просмотров."
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.MY_EMAIL]

        send_mail(subject, message, from_email, recipient_list)


class BlogCreateView(LoginRequiredMixin, CreateView):
    """Создание новой записи"""

    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование записи"""

    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_form.html"

    def get_success_url(self):
        return reverse("blog:blog_detail", kwargs={"pk": self.object.pk})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление записи"""

    model = Blog
    template_name = "blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
