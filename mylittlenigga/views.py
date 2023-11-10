from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.utils import timezone
# Create your views here.
from .forms import AdForm, Comment
from .models import Ad, Comment

class AdList(ListView):
    """
    Give list of ads
    """

    model = Ad
    context_object_name = 'ads'

class AdDetail(DetailView):
    """
    Give one ad detail
    """

    model = Ad
    context_object_name = 'ad'


class AdCreate(CreateView):
    """
    Create ad model
    """
    model = Ad
    form_class = AdForm
    template_name = 'mylittlenigga/form.html'
    success_url = '/ad/{id}'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AdUpdate(UserPassesTestMixin, UpdateView):
    """
    Update ad model View
    """
    model = Ad
    template_name = 'mylittlenigga/form.html'
    fields = ['title', 'info', 'img']

    def test_func(self):
        user = self.request.author
        object = self.get_object().author
        return user == object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = self.get_object()
        form = self.get_form_class()(instance=ad)
        context['form'] = form
        return context


class AdDelete(UserPassesTestMixin, DeleteView):
    """
    Delete ad view
    """
    model = Ad
    template_name = 'mylittlenigga/form.html'
    success_url = reverse_lazy('')

    def test_func(self):
        user = self.request.author
        object = self.get_object().author
        return user == object



class CommentCreate(CreateView):
    """
    Create ad model
    """
    model = Comment
    form_class = Comment
    template_name = 'mylittlenigga/form.html'
    success_url = ''

    def form_valid(self, form):
        form.instance.ad = get_object_or_404(Ad, pk=self.kwargs['pk'])
        return super().form_valid(form)