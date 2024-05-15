from django.db import models

# Create your models here.
class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name
class Song(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    #artist
    url = models.URLField()
    class Meta:
        verbose_name_plural = "Songs"

    def __str__(self):
        return self.name

