from django.contrib import admin
from .models import Autor, Genero, Libro, Idioma, Inventario

# Register your models here.
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Libro)
admin.site.register(Idioma)
admin.site.register(Inventario)