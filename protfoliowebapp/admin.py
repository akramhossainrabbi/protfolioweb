from django.contrib import admin
from .models import (
	Tutorials,
	Playlist,
	SidePanel
	)
# Register your models here.
admin.site.register(Tutorials)
admin.site.register(Playlist)
admin.site.register(SidePanel)