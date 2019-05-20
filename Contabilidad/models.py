from django.db import models

# Create your models here.
class Factura(models.Model):
    fecha = models.DateTimeField()
    total = models.DecimalField()

    def __str__(self):
        cadena = "Fecha:{0}    Total:{1}"
        return cadena.format( self.fecha, self.total)
