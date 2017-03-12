from django.shortcuts import render
from .models import *

def photos(request):
	photos = Photo.objects.all()
	context = {
		'photos': photos,
	}
	return render(request, 'content/photos.html', context)

def artists(request):
	artists = Artist.objects.all()
	context = {
		'artists': artists,
	}
	return render(request, 'content/artists.html', context)

def seasons(request):
	seasons = VideoSeason.objects.all()
	context = {
		'seasons': seasons,
	}
	return render(request, 'content/seasons.html', context)

def season_videos(request, season_id):
	season = VideoSeason.objects.get(id=season_id)
	videos = season.video_set.all()
	context = {
		'season': season,
		'videos': videos,
	}
	return render(request, 'content/season_videos.html', context)

def about(request):
	return render(request, 'content/about.html')