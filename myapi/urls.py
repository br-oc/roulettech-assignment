from django.urls import path
from . import views

urlpatterns = [
    path('pixel-art/', views.pixel_art, name='pixel_art'),
    path('useless-fact/', views.useless_fact, name='useless_fact'),
]
