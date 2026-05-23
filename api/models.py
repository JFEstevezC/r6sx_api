from django.db import models

class Personaje(models.Model):

    ROL_CHOICES = [
        ('Atacante', 'Atacante'),
        ('Defensor', 'Defensor'),
    ]

    VELOCIDAD_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
    ]

    DIFICULTAD_CHOICES = [
        ('Fácil', 'Fácil'),
        ('Medio', 'Medio'),
        ('Difícil', 'Difícil'),
    ]

    nombre_personaje = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='personajes/', blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    # Atributos personalizados
    organizacion = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    velocidad = models.IntegerField(choices=VELOCIDAD_CHOICES)
    dificultad = models.CharField(max_length=10, choices=DIFICULTAD_CHOICES)

    def __str__(self):
        return self.nombre_personaje

    class Meta:
        db_table = 'personajes'