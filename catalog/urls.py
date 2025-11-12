from django.urls import path

from .views import (
    ContactsView,
    HomeView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductsByCategoryView,
    ProductUpdateView,
    UnpublishProductView,
)

app_name = "catalog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product_details/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("list/", ProductListView.as_view(), name="products_list"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("product/<int:pk>/unpublish/", UnpublishProductView.as_view(), name="unpublish_product"),
    path("category/<int:category_id>/", ProductsByCategoryView.as_view(), name="products_by_category"),
]
