from django.urls import path

from .views import AddProductView, ContactsView, HomeView, ProductDetailView

app_name = "catalog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product_details/<int:pk>", ProductDetailView.as_view(), name="product_details"),
    path("add_product/", AddProductView.as_view(), name="add_product"),
]
