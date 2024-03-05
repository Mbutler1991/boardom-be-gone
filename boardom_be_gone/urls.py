"""
URL configuration for boardom_be_gone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path("basket/", include("basket.urls"), name="basket-urls"),
    path("contact/", include("contact.urls"), name="contact-urls"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:product_id>/update/', views.product_update, name='product_update'),
    path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path("saved/", include("saved.urls"), name="saved-urls"),
    path('section/<int:section_id>/subsection/<int:subsection_id>/', views.subsection_detail, name='subsection_detail'),
    path("", include("home.urls"), name="home-urls"),
]
