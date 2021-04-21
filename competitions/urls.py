from django.urls import path
from registers import views as register_views
from . import views
from .views import (CompetitionListView, 
    CompetitionDetailView,
    CompetitionCreateView,
    CompetitionUpdateView,
    CompetitionDeleteView,
    UserCompetitionListView)


# Define addition route for project .
urlpatterns = [
    #path('', views.index, name='competitions-home'),
    path('', CompetitionListView.as_view(), name='competitions-home'),
    path('user/<str:username>', UserCompetitionListView.as_view(), name='user-competitions'),
    path('competition/create', CompetitionCreateView.as_view(), name='competition-create'),
    path('competition/<int:pk>/', CompetitionDetailView.as_view(), name='competition-detail'), #pk like argument in nodejs
    path('competition/bailams/<int:pk>/', register_views.BaiLamListView.as_view(), name='register_home'),
    path('competition/bailam/<int:pk>/', register_views.BaiLamCreateView.as_view() ,name='register-bailam'),
    path('competition/<int:pk>/update', CompetitionUpdateView.as_view(), name='competition-update'),
    path('competition/<int:pk>/delete', CompetitionDeleteView.as_view(), name='competition-delete'),
    path('about/', views.about, name='competitions-about'),
]

