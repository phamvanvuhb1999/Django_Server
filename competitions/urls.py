from django.urls import path
from . import views
from .views import (CompetitionListView, 
    CompetitionDetailView,
    CompetitionCreateView,
    CompetitionUpdateView)


# Define addition route for project .
urlpatterns = [
    #path('', views.index, name='competitions-home'),
    path('', CompetitionListView.as_view(), name='competitions-home'),
    path('competition/create', CompetitionCreateView.as_view(), name='competition-create'),
    path('competition/<int:pk>/', CompetitionDetailView.as_view(), name='competition-detail'), #pk like argument in nodejs
    path('competition/<int:pk>/update', CompetitionUpdateView.as_view(), name='competition-update'),
    path('about/', views.about, name='competitions-about'),
]

