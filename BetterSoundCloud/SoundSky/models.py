from django.db import models
from django.urls import reverse
# Create your models here.
class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    followers = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="followers_rel")
    followed = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="followed_rel")
    
    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name
class Song(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #artist
    url = models.URLField()
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

