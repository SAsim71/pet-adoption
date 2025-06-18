from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('adopt/<int:pet_id>/', views.adopt_pet, name='adopt_pet'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
]
