from django.contrib import admin

from django.contrib import admin
from .models import Auto, Cliente, Problema
from .models import MiAvatarUser

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Auto)
admin.site.register(Problema)
admin.site.register(MiAvatarUser)
