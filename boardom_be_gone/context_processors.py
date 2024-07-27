from products.models import Section, Subsection, Product
from basket.models import Basket

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

def basket_count(request):
    if request.user.is_authenticated:
        basket, created = Basket.objects.get_or_create(user=request.user)
        return {'basket_count': basket.items.count()}
    return {'basket_count': 0}