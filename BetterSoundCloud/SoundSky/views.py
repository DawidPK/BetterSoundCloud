from django.shortcuts import render, get_object_or_404, redirect

from .models import *
# from .forms import *

# Create your views here.
def Profile(request, username):
    user = get_object_or_404(User, name = username)
    ctx = { 
        'Users': user
    }
    return render(request, 'SoundSky/user_page.html', ctx) 

def DetailSong(request, song_id):
    song = get_object_or_404(Song, id = song_id)
    ctx = {
        'Song': song
    }
    return render(request, 'SoundSky/song_page.html', ctx)

def Search(request):
    query = request.GET.get('search_bar', '')
    return render(request, 'Soundsky/search_page.html', {'query': query})
