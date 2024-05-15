"""
URL configuration for BetterSoundCloud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from SoundSky.views import *

urlpatterns = [
    path('', Search, name = "Home"),
    path('admin/', admin.site.urls),
    path('Profile/<str:username>', Profile, name = "Profile"),
    path("song/<int:song_id>", DetailSong, name = "Song"),
    # path("Playlist/<int:playlist_id>", Playlist, name = "Playlist"),
    # path("Playlist/<int:playlist_id>/AddSong/<int:song_id>", AddSong, name = "AddSong"),
    # path("Playlist/<int:playlist_id>/RemoveSong/<int:song_id>", RemoveSong, name = "RemoveSong"),
    # path("Playlist/<int:playlist_id>/AddUser/<str:username>", AddUser, name = "AddUser"),
    # path("Playlist/<int:playlist_id>/RemoveUser/<str:username>", RemoveUser, name = "RemoveUser"),
    # path("Playlist/<int:playlist_id>/CreatePlaylist", CreatePlaylist, name = "CreatePlaylist"),
    # path("Playlist/<int:playlist_id>/DeletePlaylist", DeletePlaylist, name = "DeletePlaylist"),
    # path("Playlist/<int:playlist_id>/RenamePlaylist", RenamePlaylist, name = "RenamePlaylist"),
    # path("Playlist/<int:playlist_id>/SharePlaylist", SharePlaylist, name = "SharePlaylist"),
    # path("Playlist/<
]
