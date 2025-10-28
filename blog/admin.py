from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "created_at")
    search_fields = (
        "title",
        "created_at",
    )
    list_filter = ("is_published",)  # фильтр по дате создания
    ordering = ("-created_at",)
