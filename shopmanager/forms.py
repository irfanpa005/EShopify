from django import forms
from shop.models import Product,Category
from django.utils.text import slugify


class ProductForm(forms.ModelForm):            
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image', 'stock', 'available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Product'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description','rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price', 'min': '1', 'step': '1'}),
            'category': forms.Select(attrs={'class': 'form-control','placeholder': 'category',}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock', 'min': '0', 'step': '1'}),
            'available': forms.CheckboxInput(attrs={'label':'available'}),
        }

    def save(self, commit=True):
        instance = super(ProductForm, self).save(commit=False)
        instance.slug = slugify(instance.name)

        if commit:
            instance.save()
        return instance
    
class CategoryForm(forms.ModelForm):            
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Category'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description','rows': 4}),
            'image': forms.FileInput(attrs={'class': 'form-control','label': 'image'}),
        }

    def save(self, commit=True):
        instance = super(CategoryForm, self).save(commit=False)
        instance.slug = slugify(instance.name)

        if commit:
            instance.save()
        return instance



