from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CreateUserForm
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
    if request.method == "POST":
        playlist_id = request.POST.get('playlist')
        playlist = Playlist.objects.get(id=playlist_id)
        song = Song.objects.get(id=song_id)
        playlist.songs.add(song)
        return redirect('Playlist', playlist_id=playlist_id)
    else:
        song = get_object_or_404(Song, id = song_id)
        playlists = Playlist.objects.all()   
        ctx = {
            'Song': song,
            'Playlists': playlists
        }
        return render(request, 'SoundSky/song_page.html', ctx)

def Search(request):
    query = request.GET.get('search_bar', '')
    songs = Song.objects.filter(name__icontains=query)
    ctx = {
        'Songs': songs
    }
    return render(request, 'Soundsky/search_page.html', ctx)

@login_required
def logout_view(request):
    logout(request)
    return redirect('Home')

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the user to the database
            # You need to authenticate the user here before logging them in
            return redirect('Home')
    else:
        form = CreateUserForm()
    return render(request, 'accounts/register.html', {'form': form})
@login_required
def create_playlist(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = User.objects.get(name=request.user)
        playlist = Playlist(name=name, user=user)
        playlist.save()
        return redirect('Playlist', playlist_id=playlist.id)
    else:
        return render(request, 'Soundsky/add_playlist.html')
@login_required
def library(request):
    user = User.objects.get(name=request.user)

    playlists = Playlist.objects.filter(user=user)
    print(playlists)
    ctx = {
        'Playlists': playlists
    }
    return render(request, 'Soundsky/library_page.html', ctx)
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Song, id = playlist_id)
    ctx = {
        'Playlist': playlist
    }
    return render(request, 'SoundSky/playlist_detail.html', ctx)


    
@login_required
def add_song_path(request):
    if request.method == "POST":
        name = request.POST.get('name')
        url = request.POST.get('url')
        song = Song(name=name, url=url)
        song.save()
        return redirect('Home')  # Replace render with redirect to return an HttpResponse object
    else:
        return render(request, 'SoundSky/add_song.html')

