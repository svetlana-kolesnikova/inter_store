from django.apps import apps
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Создаёт группу 'Модератор продуктов' и назначает права"

    def handle(self, *args, **kwargs):
        Product = apps.get_model("catalog", "Product")
        if not Product:
            self.stdout.write(self.style.WARNING("Модель Product не найдена. Команда пропущена."))
            return

        group, created = Group.objects.get_or_create(name="Модератор продуктов")
        perms_codenames = ["delete_product", "can_unpublish_product"]

        for codename in perms_codenames:
            try:
                perm = Permission.objects.get(codename=codename, content_type__app_label="catalog")
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Permission {codename} не найден."))

        self.stdout.write(self.style.SUCCESS("Группа 'Модератор продуктов' успешно создана"))
