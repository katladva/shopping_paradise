from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *
#from shopping_paradise.views import HomeView

from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path("", home, name="home"),
    path("products/", home, name="products"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)