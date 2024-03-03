from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Section, Subsection

def section_products(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    products = Product.objects.filter(sections=section)
    return render(request, 'section_products.html', {'section': section, 'products': products})

def subsection_products(request, section_id, subsection_id):
    subsection = get_object_or_404(Subsection, pk=subsection_id)
    products = Product.objects.filter(subsections=subsection)
    return render(request, 'subsection_products.html', {'subsection': subsection, 'products': products})

def section_detail(request, section_id):
    return redirect('subsection_products', section_id=section_id, subsection_id=None)

def subsection_detail(request, section_id, subsection_id):
    subsection = get_object_or_404(Subsection, pk=subsection_id)
    products = Product.objects.filter(subsections=subsection)
    return render(request, 'subsection_detail.html', {'subsection': subsection, 'products': products})