from django.contrib import admin
from .models import Dueño, Mascota, Veterinario, Consulta, Vacuna

admin.site.register(Dueño)
admin.site.register(Mascota)
admin.site.register(Veterinario)
admin.site.register(Consulta)
admin.site.register(Vacuna)
