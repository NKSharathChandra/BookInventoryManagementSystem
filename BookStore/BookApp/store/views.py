from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'store/product_detail.html', {'product': product})



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the homepage
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})