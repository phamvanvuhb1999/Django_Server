from django.shortcuts import render
from django.http import HttpResponse
from competitions.models import Competition
from django.contrib.auth.models import User


def index(request):
    competitions = Competition.objects.all()
    context = {
        'title':'Center',
        'competitions': competitions
    }
    return render(request, 'competitions/home.html', context)

def about(request):
    return render(request, 'competitions/about.html', {'title':"about"})