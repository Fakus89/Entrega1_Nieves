from django.urls import path 
from .views import taller

urlpatterns = [
    path("taller/",taller,name="taller")
]

