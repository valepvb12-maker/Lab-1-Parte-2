from django.contrib import admin
from .models import Movie


# Registramos el modelo Movie en el panel de administración
admin.site.register(Movie)
