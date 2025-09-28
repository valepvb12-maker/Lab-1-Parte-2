from django.shortcuts import render
from .models import News  # si tienes modelo News

def news_list(request):
    noticias = News.objects.all()
    return render(request, 'news.html', {'noticias': noticias})
