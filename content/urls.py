from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^photos/$', views.photos, name = 'photos'),
    url(r'^videos/$', views.seasons, name = 'seasons'),
    url(r'^videos/(?P<season_id>\d+)/$', views.season_videos, name = 'season_videos'),
    url(r'^artists/$', views.artists, name='artists'),
    url(r'^about/$', views.about, name='about'),

]