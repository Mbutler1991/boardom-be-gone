from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Section, Subsection


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
