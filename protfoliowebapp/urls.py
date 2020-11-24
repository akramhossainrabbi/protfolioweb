from django.urls import path
from .views import (
	HomeView,
	ClassesView
	)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('classes', ClassesView.as_view(), name='classes'),
]