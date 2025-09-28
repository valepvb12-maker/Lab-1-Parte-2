import json
import os
from django.core.management.base import BaseCommand
from movie.models import Movie
from django.conf import settings
from django.core.files import File

class Command(BaseCommand):
    help = "Carga películas desde movies.json a la base de datos"

    def handle(self, *args, **kwargs):
        # Ruta al archivo JSON (en la misma carpeta que este script)
        path = os.path.join(os.path.dirname(__file__), "movies.json")
        if not os.path.exists(path):
            self.stdout.write(self.style.ERROR("No se encontró movies.json"))
            return

        # Leer datos
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        # Ruta a la imagen por defecto
        default_image_path = os.path.join(settings.MEDIA_ROOT, "movie", "images", "default.jpg")
        if not os.path.exists(default_image_path):
            self.stdout.write(self.style.WARNING("⚠️ No se encontró default.jpg, se crearán pelis sin imagen."))

        # Insertar hasta 10 películas
        for i, item in enumerate(data[:10]):  # 👈 solo 10 películas
            title = item.get("title") or item.get("name") or f"Movie {i}"
            genre = item.get("genre", "Unknown")
            year = item.get("year")
            description = item.get("overview") or item.get("description") or "Sin descripción"

            movie, created = Movie.objects.get_or_create(
                title=title,
                defaults={
                    "genre": genre,
                    "year": year,
                    "description": description,
                },
            )

            # Asignar imagen por defecto si existe
            if created and os.path.exists(default_image_path):
                with open(default_image_path, "rb") as img_file:
                    movie.image.save("default.jpg", File(img_file), save=True)

        self.stdout.write(self.style.SUCCESS("Se cargaron 10 películas correctamente ✅"))
