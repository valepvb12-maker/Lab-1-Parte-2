from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie.urls')),   # la app de películas
    path('news/', include('news.urls'))  # la app de noticias
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

