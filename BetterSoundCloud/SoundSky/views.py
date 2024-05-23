from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

from .models import *
from django.contrib.auth.models import User
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

def Search(request):
    
    query = request.GET.get('search_bar', '')
    print("Tutaj am być to od debugowania: " + str(query))
    songs = Song.objects.all()
    Wong = []
    for song in songs:    
        if song.name == query:
            Wong.append(song)
    ctx = {
            'Songs':Wong
        }    
    return render(request, 'Soundsky/search_page.html', ctx)
@login_required
def logout_view(request):
    logout(request)
    return redirect('Home')

from django.contrib.auth import authenticate  # Import the authenticate function

from django.contrib.auth import authenticate  # Add the missing import statement

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the user to the database
            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # Use the authenticate function
            if user is not None:
                login(request, user)
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
        return redirect('playlist_detail', playlist_id=playlist.id)
    else:
        return render(request, 'Soundsky/add_playlist.html')
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