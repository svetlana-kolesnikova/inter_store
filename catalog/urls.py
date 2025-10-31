from django.urls import path

from .views import (
    ContactsView,
    HomeView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
)

app_name = "catalog"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product_details/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("list/", ProductListView.as_view(), name="products_list"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
