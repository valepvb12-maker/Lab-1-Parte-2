from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news'),  # vista principal de noticias
]
