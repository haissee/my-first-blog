from django.urls import path
from . import views

urlpatterns = [
    path('', views.django_countries, name='django_countries'),
]