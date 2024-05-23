from django.contrib import admin
from .models import *

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Comment)
admin.site.register(Followers)
admin.site.register(Follows)
# Register your models here.
