from django.contrib import admin

from django.contrib import admin
from .models import Auto, Cliente, Problema

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Auto)
admin.site.register(Problema)
