from products.models import Section, Subsection, Product

def sections_processor(request):
    sections = Section.objects.all()
    return {'sections': sections}

def subsections_processor(request):
    sections = Section.objects.all()
    subsections_by_section = {section: Subsection.objects.filter(section=section) for section in sections}
    return {'subsections_by_section': subsections_by_section}

def products_processor(request):
    products = Product.objects.all()  
    return {'products': products}