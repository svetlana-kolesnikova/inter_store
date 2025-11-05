from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models. EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone number")
    avatar = models.ImageField(
        upload_to='users/avatars/',
        blank=True, null=True,
        verbose_name="Add picture",
        default="img/no_image.png"
    )
    country = models.CharField(max_length=150, blank=True, null=True, verbose_name="Add country")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


    def __str__(self):
        return self.email