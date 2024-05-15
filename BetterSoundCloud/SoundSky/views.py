from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import *
# from .forms import *

# Create your views here.
@login_required
def Profile(request, username):
    user = get_object_or_404(User, name = username)
    ctx = { 
        'User': user
    }
    return render(request, 'SoundSky/user_page.html', ctx) 
@login_required
def DetailSong(request, song_id):
    song = get_object_or_404(Song, id = song_id)
    ctx = {
        'Song': song
    }
    return render(request, 'SoundSky/song_page.html', ctx)