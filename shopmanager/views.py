from django.shortcuts import get_object_or_404, redirect, render
from shop.models import Category,Product
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from . forms import ProductForm,CategoryForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
## check it the user authenticated is superuser
def is_superuser(user):
    return user.is_authenticated and user.is_superuser


@login_required
@user_passes_test(is_superuser)
def manage_store(request):
    p_form = ProductForm()
    c_form = CategoryForm()
    categories_list = Category.objects.all()
    products_list= Product.objects.all()

    paginator_p = Paginator(products_list, 20)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products=paginator_p.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator_p.page(paginator_p.num_pages)

    return render(request, 'store.html', {'products':products,'p_form':p_form,'c_form':c_form})


@login_required
@user_passes_test(is_superuser)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shopmanager:manage-store')
    else:
        return redirect('shopmanager:manage-store')
    return redirect('shopmanager:manage-store')


@login_required
@user_passes_test(is_superuser)
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    p_form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    
    if request.method == 'POST':
        if p_form.is_valid():
            p_form.save()
            return redirect('shopmanager:manage-store')

    return render(request, 'editproduct.html', {'p_form': p_form, 'product': product})


@login_required
@user_passes_test(is_superuser)
def remove_product(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('shopmanager:manage-store')


@login_required
@user_passes_test(is_superuser)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shopmanager:manage-store')
    else:
        return redirect('shopmanager:manage-store')
    return redirect('shopmanager:manage-store')


