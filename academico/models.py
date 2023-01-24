from django.db import models

class curso(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    creditos=models.PositiveSmallIntegerField()