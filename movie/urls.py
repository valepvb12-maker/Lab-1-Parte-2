from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                     # Página principal
    path('about/', views.about, name='about'),             # Página "About"
    path('statistics/', views.statistics_view, name='statistics'),  # Estadísticas
    path('signup/', views.signup, name='signup'),          # Registro
    path('login/', views.login_view, name='login'),        # Login (aunque sea en construcción)
]
