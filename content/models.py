from __future__ import unicode_literals
from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=200, default = 'brooklyn_img')
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field='width', height_field='height')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']

class Artist(models.Model):
    name = models.CharField(max_length=150)
    about = models.TextField()
    life_image = models.ImageField(null=False, blank=False)
    serial_image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name

class VideoSeason(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.title

class Video(models.Model):
    episode = models.IntegerField(default=0)
    season = models.ForeignKey(VideoSeason)
    video = models.FileField()

    def __str__(self):
        return str(self.episode)