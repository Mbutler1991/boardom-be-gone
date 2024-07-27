from django.urls import path
from . import views

urlpatterns = [
    path('save_for_later/<int:product_id>/', views.save_for_later, name='save_for_later'),
    path('saved_for_later/', views.saved_for_later, name='saved_for_later'),
    path('remove_from_saved/<int:saved_id>/', views.remove_from_saved, name='remove_from_saved'),
]