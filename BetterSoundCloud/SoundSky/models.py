from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
# class User(models.Model):

#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100, unique=True)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     followers = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="followers_rel")
#     followed = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="followed_rel")
    
#     class Meta:
#         verbose_name_plural = "Users"

#     def __str__(self):
#         return self.name
class Followers(models.Model):
    user_being_followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed", primary_key=True)
    followers = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="followers_rel")
    class Meta:
        verbose_name_plural = "Followers"

    def __str__(self):
        return str(self.user_being_followed)
class Follows(models.Model):
    user_that_follows = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers", primary_key=True)
    users_being_followed = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="followed_rel")
    class Meta:
        verbose_name_plural = "Follows"

    def __str__(self):
        return str(self.user_that_follows)
class Song(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #artist
    url = models.URLField()
    # Playlist = models.ManyToManyField("Playlist", blank=True)
    def get_absolute_url(self):
        return reverse("Song", kwargs={"song_id": self.id})
    class Meta:
        verbose_name_plural = "Songs"

    def __str__(self):
        return self.name
    


class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    def get_absolute_url(self):
        return reverse("Playlist", kwargs={"playlist_id": self.id})
    class Meta:
        verbose_name_plural = "Playlists"

    def __str__(self):
        return self.name
        
class Comment(models.Model):
        id = models.AutoField(primary_key=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        song = models.ForeignKey(Song, on_delete=models.CASCADE)
        content = models.TextField()
        
        class Meta:
            verbose_name_plural = "Comments"
    
        def __str__(self):
            return self.content

