from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Personaje
from .serializers import PersonajeSerializer
from .filters import PersonajeFilter
from .pagination import PersonajePagination

class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PersonajeFilter
    ordering_fields = ['nombre_personaje', 'velocidad']
    ordering = ['nombre_personaje']
    pagination_class = PersonajePagination