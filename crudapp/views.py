from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    print(products)
    context = {
        "products": products,
    }
    return render(request, "product_list.html", context)

def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
    }
    return render(request, "product_details.html", context)

def product_create(request):
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("crudapp:product_list"))
    else:
        form = ProductForm()

    context = {
        "form": form,
    }
    return render(request, "product_form.html", context)

def product_update(request, pk):
    product_obj = get_object_or_404(Product, pk=pk)
    if request.method=="POST":
        form = ProductForm(instance=product_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("crudapp:product_details", args=[pk, ]))
        
    else:
        form = ProductForm(instance=product_obj)

    context = {
        "form": form,
        "object": product_obj
    }
    return render(request, 'product_form.html', context)

def product_delete(request, pk):
    product_obj = get_object_or_404(Product, pk=pk)
    product_obj.delete()
    return redirect(reverse("crudapp:product_list"))