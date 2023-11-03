from django.urls import path

from . import views

app_name = 'shopmanager'
urlpatterns = [
    path('managestore/', views.manage_store, name='manage-store'),
    path('addproduct/', views.add_product, name='add-product'),
    path('editproduct/<int:product_id>', views.edit_product, name='edit-product'),
    path('removeproduct/<int:product_id>', views.remove_product, name='remove-product'),
    path('addcategory/', views.add_category, name='add-category'),
]
