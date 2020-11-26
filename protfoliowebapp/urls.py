from django.urls import path
from .views import (
	HomeView,
	ClassesView,
	TutorialView
	)
app_name = 'protfolioweb'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('classes', ClassesView.as_view(), name='classes'),
    path('playlist/<int:pk>', TutorialView.as_view(), name='tutorial_list'),
]