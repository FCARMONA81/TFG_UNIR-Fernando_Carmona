# myapp/admin.py

from django.contrib import admin
from .models import UGC, AGC, Objetivo, Indicador, AcuerdoIndicadores, Usuario

admin.site.register(UGC)
admin.site.register(AGC)
admin.site.register(Objetivo)
admin.site.register(Indicador)
admin.site.register(AcuerdoIndicadores)
admin.site.register(Usuario)
