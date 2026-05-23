import django_filters
from .models import Personaje

class PersonajeFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(
        field_name='nombre_personaje', 
        lookup_expr='icontains'
    )
    organizacion = django_filters.CharFilter(
        field_name='organizacion', 
        lookup_expr='icontains'
    )
    rol = django_filters.CharFilter(
        field_name='rol', 
        lookup_expr='iexact'
    )

    class Meta:
        model = Personaje
        fields = ['nombre', 'organizacion', 'rol']