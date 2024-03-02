from django.shortcuts import render
from .models import Product, Section, Subsection

def section_products(request, section_id):
    section = Section.objects.get(pk=section_id)
    products = Product.objects.filter(sections=section)
    return render(request, 'section_products.html', {'section': section, 'products': products})

def subsection_products(request, section_id, subsection_id):
    subsection = Subsection.objects.get(pk=subsection_id)
    products = Product.objects.filter(subsections=subsection)
    return render(request, 'subsection_products.html', {'subsection': subsection, 'products': products})