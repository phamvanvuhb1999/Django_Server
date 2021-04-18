from django.urls import path
from . import views


# Define addition route for project .
urlpatterns = [
    path('', views.index, name='competitions-home'),
    path('about/', views.about, name='competitions-about'),
]