from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
from news.models import News  
def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    total_movies = Movie.objects.count()
    total_news = News.objects.count()

    return render(request, 'home.html', {
        'searchTerm': searchTerm,
        'movies': movies,
        'total_movies': total_movies,
        'total_news': total_news,
    })
def about(request):
    return render(request, 'about.html')
import matplotlib
matplotlib.use('Agg')   
import matplotlib.pyplot as plt
import io, base64
def statistics_view(request):
    all_movies = Movie.objects.all()
    counts_by_year = {}
    for m in all_movies:
        year = m.year if m.year else "Unknown"
        counts_by_year[year] = counts_by_year.get(year, 0) + 1
    years = sorted(counts_by_year.keys())
    year_counts = [counts_by_year[y] for y in years]
    counts_by_genre = {}
    for m in all_movies:
        genre = m.genre if m.genre else "Unknown"
        counts_by_genre[genre] = counts_by_genre.get(genre, 0) + 1
    genres = sorted(counts_by_genre.keys())
    genre_counts = [counts_by_genre[g] for g in genres]
    fig1, ax1 = plt.subplots()
    ax1.bar(years, year_counts)
    ax1.set_title('Películas por año')
    plt.tight_layout()
    buf1 = io.BytesIO()
    fig1.savefig(buf1, format='png')
    plt.close(fig1)
    buf1.seek(0)
    image_year = base64.b64encode(buf1.getvalue()).decode('utf-8')
    buf1.close()
    fig2, ax2 = plt.subplots()
    ax2.bar(genres, genre_counts)
    ax2.set_title('Películas por género')
    plt.tight_layout()
    buf2 = io.BytesIO()
    fig2.savefig(buf2, format='png')
    plt.close(fig2)
    buf2.seek(0)
    image_genre = base64.b64encode(buf2.getvalue()).decode('utf-8')
    buf2.close()
    total_movies = Movie.objects.count()
    total_news = News.objects.count()
    return render(request, 'statistics.html', {
        'image_year': image_year,
        'image_genre': image_genre,
        'total_movies': total_movies,
        'total_news': total_news,
    })
from django.shortcuts import redirect

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # aquí podrías guardar email en base de datos o mostrar un mensaje
        return redirect('home')  # vuelve a home al enviar
    return render(request, 'signup.html')  # 👈 asegúrate que diga signup.html

def login_view(request):
    return render(request, 'login.html')


def signup(request):
    email = None
    if request.method == 'POST':
        email = request.POST.get('email')
        # aquí podrías guardar email en base de datos si quieres
    return render(request, 'signup.html', {'email': email})
