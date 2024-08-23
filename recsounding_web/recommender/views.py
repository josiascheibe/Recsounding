# É um componente central responsavel por definir a lógica de controle da aplicação. Lida com as requisições dos usuários e retorna as respostas apropriadas.
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Song

from .signals import song_played

# Create your views here.
def index(request):
    messages.success(request, "Welcome to Recsounding!")
    return render(request, "index.html")


def recommend(request):
    recommendations = Song.objects.filter(is_featured=True).order_by("-release_date")
    paginator = Paginator(recommendations, 10)  # Mostra 10 musicas por pagina

    page_number = request.GET.get("page")
    recommendations = paginator.get_page(page_number)

    if not recommendations:
        messages.error(request, "No recommendations available at the moment")
    return render(request, "recommend.html", {"recommendations": recommendations})

#Signals.py handle_song_played def
def play_song(request, song_id):
    song = Song.objects.get(id = song_id)
    song_played.send(sender=Song, instance=song, user=request.user)