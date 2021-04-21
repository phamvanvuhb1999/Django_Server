from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from competitions.models import Competition
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
    DetailView,
    CreateView, 
    UpdateView, 
    DetailView,
    DeleteView)

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
    paginate_by = 10

#define detail competition
class CompetitionDetailView(DetailView):
    model = Competition

#add mixin for require user logged in
class CompetitionCreateView(LoginRequiredMixin, CreateView):
    model = Competition
    fields = ['name', 'description', 'exam_lo', 'time_limit', 'start_time', 'time_for_testing']

    #override form_valid function to add current login user is competitions author
    def form_valid(self, form, **kwargs):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CompetitionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Competition
    fields = ['name', 'description', 'exam_lo', 'time_limit', 'start_time', 'time_for_testing']

    #override form_valid function to add current login user is competitions author, with mixin
    def form_valid(self, form, **kwargs):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self, *args, **kwargs):
        post = self.get_object() #get competition currently try to update
        if self.request.user == post.created_by:
            return True
        return False

class CompetitionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Competition

    #add success url to redirect when delete competition
    success_url = 'competitions-home'

    def test_func(self, *args, **kwargs):
        post = self.get_object() #get competition currently try to update
        if self.request.user == post.created_by:
            return True
        return False

class UserCompetitionListView(ListView):
    model = Competition
    template_name = 'competitions/user_posts.html'
   
    context_object_name = 'competitions'
    paginate_by = 10


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) #get username from url
        return Competition.objects.filter(created_by=user).order_by('start_time')


def about(request):
    return render(request, 'competitions/about.html', {'title':"about"})

