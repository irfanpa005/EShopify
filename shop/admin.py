from django.contrib import admin
from .models import Product, Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} #to automatically populate the value of slug based on name
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)} #to automatically populate the value of slug based on name
    list_per_page = 20
admin.site.register(Product, ProductAdmin)