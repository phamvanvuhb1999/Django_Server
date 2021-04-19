from django.shortcuts import render
from django.http import HttpResponse
from competitions.models import Competition
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
    DetailView,
    CreateView, 
    UpdateView, 
    DetailView)

#handle homepage
def index(request):
    competitions = Competition.objects.all()
    context = {
        'title':'Center',
        'competitions': competitions
    }
    return render(request, 'competitions/home.html', context)
#like index
class CompetitionListView(ListView):
    model = Competition
    #define template file
    template_name = 'competitions/home.html'
   
    context_object_name = 'competitions'
    #oder list competitions
    ordering = ['start_time']

#define detail competition
class CompetitionDetailView(DetailView):
    model = Competition

#add mixin for require user logged in
class CompetitionCreateView(LoginRequiredMixin, CreateView):
    model = Competition
    fields = ['name', 'description', 'exam_lo', 'time_limit', 'start_time', 'time_for_testing']

    #override form_valid function to add current login user is competitions author
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CompetitionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Competition
    fields = ['name', 'description', 'exam_lo', 'time_limit', 'start_time', 'time_for_testing']

    #override form_valid function to add current login user is competitions author, with mixin
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object() #get competition currently try to update
        if self.request.user == post.created_by:
            return True
        return False

    
def about(request):
    return render(request, 'competitions/about.html', {'title':"about"})

