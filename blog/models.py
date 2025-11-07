from django.conf import settings
from django.db import models


class Blog(models.Model):
    """Модель блоговой записи"""

    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Содержимое")
    preview = models.ImageField(
        "Превью", upload_to="blog_previews/", blank=True, null=True, default="img/no_image.png"
    )

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    is_published = models.BooleanField("Опубликовано", default=False)
    views_count = models.PositiveIntegerField("Количество просмотров", default=0)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ["-created_at"]
        permissions = [
            ("can_publish_blog", "Может публиковать блог"),
        ]
