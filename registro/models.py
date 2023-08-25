from django.db import models

# Create your models here.

class registro(models.Model):
    nombre      =   models.CharField(max_length=50, blank=True, null=True)
    apellido    =   models.CharField(max_length=50, blank=True, null=True)
    documento   =   models.CharField(max_length=50, blank=True, null=True)
    numCredito  =   models.CharField(max_length=50, blank=True, null=True)
    created     =   models.DateTimeField(auto_now_add=True)
    updated     =   models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Registro'
        verbose_name_plural='Registros'

    def __str__(self):
        return self.documento