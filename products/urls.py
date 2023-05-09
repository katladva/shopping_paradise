from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("products/", products, name="products"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
]