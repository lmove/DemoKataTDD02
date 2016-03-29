from django.contrib import admin
from .models import Servicio
from .models import Independiente
from .models import Comentario

# Jd.Runza Registro de modelos
# Register your models here.

admin.site.register(Servicio)

admin.site.register(Independiente)

admin.site.register(Comentario)
