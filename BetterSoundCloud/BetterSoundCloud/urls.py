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
    path('Profile', Profile, name = "Profile"),
    path("Song/<int:song_id>", DetailSong, name = "Song"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('Profile/Library/Add/Playlist', create_playlist, name='Add Playlist'),
    path('Profile/Library/', library, name="Library"),
    path("Playlist/<int:playlist_id>", playlist_detail, name = "Playlist"),
    path("AddSong", add_song_path, name = "AddSong"),
    path("Profile/<str:username>", user_profile, name = "User"),
    path("Follow/<str:username>", follow, name = "Follow"),
    # ...
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
