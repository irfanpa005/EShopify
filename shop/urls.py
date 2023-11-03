from django.contrib import admin
from django.urls import path, include
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<slug:c_slug>/', views.all_products, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

]
