# myapp/models.py

from django.db import models
from decimal import Decimal

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id_ugc = models.ForeignKey('UGC', on_delete=models.CASCADE, null=True, blank=True)
    descripcion_usuario = models.CharField(max_length=255, blank=True, null=True)
    perfil = models.CharField(max_length=255, blank=True, null=True)
    fecha_crea_usuario = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

class UGC(models.Model):
    id_ugc = models.AutoField(primary_key=True)
    nombre_ugc = models.CharField(max_length=255)
    descripcion_ugc = models.CharField(max_length=255, blank=True, null=True)
    responsable_ugc = models.CharField(max_length=255, blank=True, null=True)
    fecha_crea_ugc = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre_ugc

class AGC(models.Model):
    id_agc = models.AutoField(primary_key=True)
    descripcion_agc = models.CharField(max_length=255, blank=True, null=True)
    anio_agc = models.IntegerField()
    id_ugc = models.ForeignKey(UGC, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descripcion_agc} ({self.anio_agc})"

class Objetivo(models.Model):
    id_objetivo = models.AutoField(primary_key=True)
    nombre_objetivo = models.CharField(max_length=255)
    descripcion_objetivo = models.CharField(max_length=255, blank=True, null=True)
    perspectiva = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre_objetivo

class Indicador(models.Model):
    id_indicador = models.AutoField(primary_key=True)
    id_objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)
    nombre_indicador = models.CharField(max_length=255)
    descripcion_indicador = models.CharField(max_length=255, blank=True, null=True)
    fuente = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_indicador

class AcuerdoIndicadores(models.Model):
    id_acuerdo_indicador = models.AutoField(primary_key=True)
    id_agc = models.ForeignKey(AGC, on_delete=models.CASCADE)
    id_indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    valor_min = models.DecimalField(max_digits=10, decimal_places=2)
    valor_opt = models.DecimalField(max_digits=10, decimal_places=2)
    valor_obtenido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    peso_indicador = models.DecimalField(max_digits=10, decimal_places=2)
    resultado_indicador = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    porcentaje_conseguido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calcula el valor_obtenido basado en resultado_indicador
        if self.valor_obtenido is None:
            self.resultado_indicador = None
        else:
            valor_obtenido_float = float(self.valor_obtenido)
            valor_opt_float = float(self.valor_opt)
            valor_min_float = float(self.valor_min)
            peso_indicador_float = float(self.peso_indicador)

            if valor_obtenido_float  >= valor_opt_float:
                self.resultado_indicador = peso_indicador_float
                self.porcentaje_conseguido = Decimal('100')
            elif valor_obtenido_float  <= valor_min_float:
                self.resultado_indicador = Decimal('0')
                self.porcentaje_conseguido = Decimal('0')
            else:
                self.resultado_indicador = Decimal((valor_obtenido_float - valor_min_float) / (valor_opt_float - valor_min_float) * peso_indicador_float)
                self.porcentaje_conseguido = (self.resultado_indicador / self.peso_indicador) * Decimal('100')

        # Calcula el porcentaje_conseguido basado en resultado_indicador y peso_indicador
        

        super(AcuerdoIndicadores, self).save(*args, **kwargs)


    def __str__(self):
        return f"Indicador {self.id_indicador} en AGC {self.id_agc}"
    

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    descripcion_usuario = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=255)
    psw = models.CharField(max_length=255)
    perfil = models.CharField(max_length=255)
    id_ugc = models.ForeignKey(UGC, on_delete=models.CASCADE)
    fecha_crea_usuario = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre_usuario
