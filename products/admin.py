from .models import Product, Section, Subsection
from django.contrib import admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'in_stock')
    search_fields = ('name', 'description')
    list_filter = ('in_stock',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Subsection)
class SubsectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'section')
    list_filter = ('section',)
