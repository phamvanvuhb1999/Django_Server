from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from competitions.models import Competition
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from registers.models import Register, BaiLam
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone


# Create your views here.
@login_required
#@user_passes_test
def registers_test(request, *args, **kwargs):
    # test_func = def test_func(user, competition):
    #     if competition.user_id == user:
    #         return False
    #     return true
    redirect_field_name ='/'
    userr = request.user
    competition_id = request.GET['competition'][0]
    competition = Competition.objects.filter(id=competition_id).first()

    if userr and competition:
        #check register added to db
        temp = Register.objects.filter(user_id=userr, competition_id=competition).first()
        competition_start_time = Competition.objects.filter(id=competition_id).first().start_time
        date_now = timezone.now()
        if temp or date_now >= competition_start_time:
            print('Register is exist.')
        else:
            regist = Register.objects.create(user_id=userr, competition_id=competition)
            regist.save()
            messages.success(request, f'Add new competition success.')
            return redirect('/')

    #messages.success(request, f'New competition not be add.')
    messages.warning(request, f'You was already join to Contest or Contest is already Started.')
    return redirect('/')
    print("competition_id: " + competition_id)
    return redirect('competitions-home')

    #<QueryDict: {'competition': ['2']}>
    
from django.views.generic import (ListView,
    DetailView,
    CreateView, 
    UpdateView, 
    DetailView,
    DeleteView)


class BaiLamListView(LoginRequiredMixin ,ListView):
    model = BaiLam
    #define template file
    template_name = 'bailams/home.html'
   
    context_object_name = 'bailams'

    def get_queryset(self):
        #get competition info from URL_INFO
        competition_id = self.request.META.get('PATH_INFO').split('/')
        competition_id = competition_id[len(competition_id) - 2]
        return BaiLam.objects.filter(competition_id=competition_id).order_by('percent')


    def get(self, request, *args, **kwargs):
        context = locals()
        competition_id = self.request.META.get('PATH_INFO').split('/')
        competition_id = competition_id[len(competition_id) - 2]
        context['contest_id'] = competition_id
        context['contest_name'] = Competition.objects.filter(id=competition_id).first().name
        context['bailams'] = self.get_queryset()
        

        return render(request, 'bailams/home.html', context)


class BaiLamCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = BaiLam
    fields = ['trained_model', 'test_code']
    template_name = 'bailams/bailam_form.html'

    def form_valid(self, form, **kwargs):
        form.instance.user_id = self.request.user
        form.instance.competition_id = self.request
        return super().form_valid(form)

    def test_func(self, *args, **kwargs):
        #check user is already join 
        user_id = self.request.user
        competition_id = self.request.META.get('PATH_INFO').split('/')
        competition_id = competition_id[len(competition_id) - 2]
        competition_id = Competition.objects.filter(id=competition_id).first()
        flag = Register.objects.filter(user_id=user_id, competition_id=competition_id).first()
        if flag is None:
            return False
        return True