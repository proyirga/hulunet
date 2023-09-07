from typing import Any, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponse
from . models import Item4Rent   


def rent(request):

    context = {
        'rents': Item4Rent.objects.all()
    }
    return render(request, 'rents/rents.html', context)


class Item4RentListView(ListView):
    model = Item4Rent
    template_name = 'rents/rents.html'
    context_object_name = 'rents'
    paginate_by = 5


class UserRentsListView(ListView):
    model = Item4Rent
    template_name = 'rents/item4rent_list.html'
    context_object_name = 'rents'
    paginate_by = 5


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Item4Rent.objects.filter(posted_by=user).order_by('-date_posted')


class RentDetailView(DetailView):
    model = Item4Rent


class RentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item4Rent
    success_url = '/'


    def test_func(self):
        rent = self.get_object()
        if self.request.user == rent.posted_by:
            return True 
        return False


class RentCreateView(LoginRequiredMixin, CreateView):
    model = Item4Rent
    fields = ['item_name', 'image', 'description', 'location', 'cost']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)



class RentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item4Rent
    fields = ['image', 'item_name', 'cost', 'description', 'location', 'rented']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        rent = self.get_object()
        if self.request.user == rent.posted_by:
            return True 
        return False