from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Tutorials(models.Model):
    video_header = models.CharField(max_length=1000)
    video_url = models.URLField(max_length=1000)
    details = models.TextField()

class Playlist(models.Model):
    tutorial = models.ForeignKey(Tutorials, on_delete=models.CASCADE)
    video_header = models.CharField(max_length=1000)
    video_url = models.URLField(max_length=1000)
    release_date = models.DateField()

class SidePanel(models.Model):
	header = models.CharField(max_length=300)
	details = models.TextField()
		