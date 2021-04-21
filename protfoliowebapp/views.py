from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import (
	Tutorials, 
	SidePanel,
	Playlist
	)

# Create your views here.
class HomeView(TemplateView):
   template_name = 'protfolioweb/index.html'

class ClassesView(View):
 
   def get(self, request, *args, **kwargs):
        all_tutorials = Tutorials.objects.all()
        side_panel_blogs = SidePanel.objects.all()
        context = {
        'all_tutorials': all_tutorials,
        'side_panel_blogs': side_panel_blogs
        }
        return render(request, 'protfolioweb/classes.html', context)

class TutorialView(TemplateView):
	def get(self, request, pk, *args, **kwargs):
		tutorials_playlist = Playlist.objects.filter(pk=pk)
		context = {'tutorials_playlist': tutorials_playlist}
		return render(request, 'protfolioweb/tutorials.html', context)

class ServiceView(TemplateView):
   template_name = 'protfolioweb/services.html'

class ContactView(TemplateView):
   template_name = 'protfolioweb/contact.html'
    