from django.contrib import admin
from .models import Personaje

@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_personaje', 'organizacion', 'rol', 'velocidad', 'dificultad']
    list_filter = ['rol', 'organizacion', 'dificultad']
    search_fields = ['nombre_personaje']