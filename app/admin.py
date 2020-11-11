from django.contrib import admin
from .models import Transferencia
# Register your models here.


class TransferenciaAdm(admin.ModelAdmin):
    list_display = ["nombreDeposita", "nombreRecibe", "monto", "codigo", "imagenCarnet"]

admin.site.register(Transferencia, TransferenciaAdm)