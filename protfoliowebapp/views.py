from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Tutorials, SidePanel

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