from django.contrib import admin
from .models import Photo, Artist, Video, VideoSeason

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp']

    class Meta:
        model = Photo

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Artist)
admin.site.register(Video)
admin.site.register(VideoSeason)