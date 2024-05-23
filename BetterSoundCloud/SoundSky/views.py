from __future__ import print_function
import re
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

from .models import *
from django.contrib.auth.models import User
from .models import Followers, Follows
# from .forms import *

# Create your views here.

def Profile(request):
    user = request.user
    followers = Followers.objects.get(user_being_followed=user)
    follows = Follows.objects.get(user_that_follows=user)
    follower_count = followers.followers.count()
    following_count = follows.users_being_followed.count()
    ctx = { 
        'User': user,
        'Followers': follower_count,
        'Following': following_count
    }
    return render(request, 'SoundSky/user_page.html', ctx) 
# @login_required
def DetailSong(request, song_id):
    if request.method == "POST":
        playlist_id = request.POST.get('plays')
        playlist = Playlist.objects.get(id=playlist_id)
        song = Song.objects.get(id=song_id)
        playlist.songs.add(song)
        return redirect('Song', song_id=song_id)
    else:
        song = get_object_or_404(Song, id = song_id)
        playlists = Playlist.objects.filter(user=request.user)   
        ctx = {
            'Song': song,
            'Playlists': playlists
        }
        return render(request, 'SoundSky/song_page.html', ctx)

def Search(request):
    query = request.GET.get('search_bar', '')
    songs = Song.objects.filter(name__icontains=query)
    users = User.objects.filter(username__icontains=query)
    playlists = Playlist.objects.filter(name__icontains=query)
    ctx = {
        'Songs': songs,
        'Users': users,
        'Playlists': playlists
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
            user = form.save()
            # This saves the user to the database
            # Create followers and followed in database with the same primary key as user
            followers = Followers(user_being_followed=user)
            followers.save()
            follows = Follows(user_that_follows=user)
            follows.save()
            # You need to authenticate the user here before logging them in
            login(request, user)
            return redirect('Home')
    else:
        form = CreateUserForm()
    return render(request, 'accounts/register.html', {'form': form})
@login_required
def create_playlist(request):
    if request.method == "POST":
        name = request.POST.get('name')
        user = request.user
        playlist = Playlist(name=name, user=user)
        playlist.save()
        return redirect('Library')
    else:
        return render(request, 'Soundsky/add_playlist.html')
@login_required
def library(request):
    user = request.user

    playlists = Playlist.objects.filter(user=user)
    print(playlists)
    ctx = {
        'Playlists': playlists
    }
    return render(request, 'Soundsky/library_page.html', ctx)
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id = playlist_id)
    songs = playlist.songs.all()
    ctx = {
        'Playlist': playlist,
        'Songs': songs
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
def user_profile(request, username):
    user = User.objects.get(username=username)
    follows = Follows.objects.get(user_that_follows=request.user)
    followers = Followers.objects.get(user_being_followed=user)
    follower_count = followers.followers.count()
    following_count = follows.users_being_followed.count()
    ctx = {
        'OtherUser': user,
        'Followers': follower_count,
        'Following': following_count
    }
    return render(request, 'SoundSky/other_user_page.html', ctx)
def follow(request, username):
    user = request.user
    user_to_follow = User.objects.get(username=username)
    follows = Follows.objects.get(user_that_follows=user)
    follows.users_being_followed.add(user_to_follow)
    follows.save()
    followers = Followers.objects.get(user_being_followed=user_to_follow)
    followers.followers.add(user)
    followers.save()
    return redirect('User', username=username)