from django.db import models

class POI(models.Model):
    nome = models.CharField(max_length=50)
    coord_x = models.PositiveIntegerField()
    coord_y = models.PositiveIntegerField()