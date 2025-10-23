"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from xml.etree.ElementInclude import include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from catalog import views
from catalog.views import add_product

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # ✅ теперь главная страница — home()
    path("contacts/", views.contacts, name="contacts"),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("product_details/", views.product_details),
    path("add_product/", add_product, name="add_product"),
]

# Добавляем поддержку статики и медиа при DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
