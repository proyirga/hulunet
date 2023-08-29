from typing import Optional
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponse
from .models import Jobs
from django.contrib.auth.models import User



def jobportal(request):

    context = {
        'jobs': Jobs.objects.all()
    }
    return render(request, 'jobportal/jobs.html', context)


class JobtListView(ListView):
    model = Jobs
    template_name = 'jobportal/jobs.html'
    context_object_name = 'jobs'
    ordering = ['-date_posted']
    paginate_by = 5


class JobDetailView(DetailView):
    model = Jobs



class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Jobs
    success_url = 'jobs/'


    def test_func(self):
        job = self.get_object()
        if self.request.user == job.posted_by:
            return True 
        return False

class JobCreateView(LoginRequiredMixin, CreateView):
    model = Jobs
    template_name = 'jobportal/job_form.html'
    fields = ['job_title', 'organization', 'location', 'salary', 'job_description']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)



class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Jobs
    fields = ['job_title', 'job_description']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
            return True 
        return False
