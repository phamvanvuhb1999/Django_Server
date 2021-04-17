from django.urls import path
from . import views


# Define addition route for project .
urlpatterns = [
    path('', views.home, name='competions-home'),
    path('about/', views.about, name='competitions-about'),
]