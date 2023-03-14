from django.urls import path
from . import views

app_name="crudapp"

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('product-details/<int:pk>/', views.product_details, name="product_details"),
    path("product-create/", views.product_create, name="product_create"),
    path("product-update/<int:pk>", views.product_update, name="product_update"),
    path("product-delete/<int:pk>", views.product_delete, name="product_delete"),
]