from django.db import models

# Create your models here.
class Transferencia(models.Model):
    nombreDeposita = models.CharField(max_length=50)
    nombreRecibe = models.CharField(max_length=50)
    monto = models.IntegerField()
    codigo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreDeposita


