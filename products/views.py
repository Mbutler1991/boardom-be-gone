from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import os
from .models import Product, Section, Subsection
from .forms import ProductForm
import cloudinary.uploader


def section_detail(request, section_id):
    return redirect('subsection_products', section_id=section_id, subsection_id=None)

def subsection_detail(request, section_id, subsection_id):
    subsection = get_object_or_404(Subsection, pk=subsection_id)
    products = Product.objects.filter(subsections=subsection)
    return render(request, 'subsection_detail.html', {
        'subsection': subsection, 
        'products': products
        })

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

@login_required
@staff_member_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            image_file = request.FILES.get('image')
            if image_file:
                cloudinary.config(cloudinary_url=os.environ.get('CLOUDINARY_URL'))
                upload_result = cloudinary.uploader.upload(image_file)
                form.instance.image = upload_result['secure_url']
            form.save()
            return redirect('home') 
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})

@login_required
@staff_member_required
def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            image_file = request.FILES.get('image')
            if image_file:
                cloudinary.config(cloudinary_url=os.environ.get('CLOUDINARY_URL'))
                upload_result = cloudinary.uploader.upload(image_file)
                product.image = upload_result['secure_url']
            form.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_update.html', {'form': form, 'product': product})

@login_required
@staff_member_required
def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')  
    return render(request, 'product_delete.html', {'product': product})