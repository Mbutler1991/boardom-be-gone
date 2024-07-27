from django.urls import path
from . import views

urlpatterns = [
    path('add_to_basket/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('view_basket/', views.view_basket, name='view_basket'),
    path('remove_from_basket/<int:basketitem_id>/', views.remove_from_basket, name='remove_from_basket'),
]