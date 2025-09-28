import pandas as pd
import os
import django

# Configurar Django para que este script pueda usar los modelos
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviereviews.settings')
django.setup()

from movie.models import Movie

# Ruta del CSV
csv_file = 'movies_initial.csv'

# Leer CSV
df = pd.read_csv(csv_file)

# Imagen por defecto para todas las películas
default_image = 'movie/images/default.jpg'

# Crear las películas en la base de datos
for index, row in df.iterrows():
    Movie.objects.create(
        title=row['title'],
        genre=row['genre'],
        year=row['year'],
        description=row['description'],
        image=default_image
    )

print("Películas cargadas con éxito.")
