from .views import (
    HomeView,
    CreateWebsite,
    Dashboard,
    WebsiteInfo,
    UpdateView,
    AddtoWebsite,
    RemoveFromWebsite,
    CreateProductView,
    UpdateProductView,
    DeleteProductView,
    DeleteWebsiteView,
    ProductInfo,
)

from django.urls import path

urlpatterns = [
    path('', HomeView, name='home'),
    path('create-website/', CreateWebsite, name="create"),
    path('dashboard/', Dashboard, name="dashboard"),
    path('website/<str:pk>/', WebsiteInfo, name="website-info"),
    path('update/<str:pk>/', UpdateView, name="update"),
    path('delete/<str:pk>/', DeleteWebsiteView, name="delete"),
    path('add/<str:product_id>/to/<str:website_id>/', AddtoWebsite, name="add"),
    path('remove/<str:product_id>/from/<str:website_id>/', RemoveFromWebsite, name="remove"),
    path('create-product/', CreateProductView, name="create-product"),
    path('update-product/<str:pk>/', UpdateProductView, name="update-product"),
    path('delete-product/<str:pk>/', DeleteProductView, name="delete-product"),
    path('product/<str:pk>/', ProductInfo, name="product-info"),
]
